from .constants import (
    UNASSIGNED,
    ADMIN,
    DRIVER,
    EMPLOYEE,
    SECRETARY,
    EXCLUDE,
    ONLY,
)


def reservation_to_dict(reservation):
    reservation_dict = reservation.to_dict()
    stop_list = []
    stops = reservation.stops.all()
    if reservation.company:
        reservation_dict["company"] = reservation.company.to_dict()
    else:
        reservation_dict["company"] = {}
    if reservation.driver:
        reservation_dict["driver"] = reservation.driver.to_dict()
    else:
        reservation_dict["driver"] = {}
    for stop in stops:
        employee = stop.employee
        stop_dict = stop.to_dict()
        stop_dict["employee_full_name"] = employee.full_name
        stop_list.append(stop_dict)
    reservation_dict["stops"] = stop_list

    return reservation_dict


def invoice_to_dict(invoice):
    invoice_dict = invoice.to_dict()
    items = invoice.items.all()
    invoice_dict["items"] = []
    for item in items:
        item_dict = item.to_dict()
        invoice_dict["items"].append(item_dict)
    if invoice.reservation.destination:
        invoice_dict["destination"] = invoice.reservation.destination
    else:
        invoice_dict["destination"] = ""

    return invoice_dict


def driver_to_dict(driver):
    reservation_list = []
    for reservation in driver.reservations.all():
        reservation_list.append(reservation.to_dict())
    driver_dict = driver.to_dict()
    driver_dict["reservations"] = reservation_list

    return driver_dict


def user_to_dict(user, serialization_type):
    """Check for role"""
    user_dict = {}
    if serialization_type == ONLY:
        user_dict = user.to_dict(only=serialization_type)
    if serialization_type == EXCLUDE:
        user_dict = user.to_dict(exclude=serialization_type)
    role = UNASSIGNED
    role_id = "no_id"
    role_name = "no_name"
    if user.admin:
        role = ADMIN
        role_id = user.admin.id
        role_name = user.admin.full_name
    if user.driver:
        role = DRIVER
        role_id = user.driver.id
        role_name = user.driver.full_name
    if user.employee:
        role = EMPLOYEE
        role_id = user.employee.id
        role_name = user.employee.full_name
    if user.secretary:
        role = SECRETARY
        role_id = user.secretary.id
        role_name = user.secretary.full_name
        role_secretary = user.secretary.role
        user_dict["role_secretary"] = role_secretary
    user_dict["role"] = role
    user_dict["role_id"] = role_id
    user_dict["role_name"] = role_name

    return user_dict
