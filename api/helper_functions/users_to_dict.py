from .constants import EXCLUDE_CREATE


def entity_to_dict(user):
    if user.admin:
        entity_dict = user.admin.to_dict()
    if user.driver:
        entity_dict = user.driver.to_dict()
    if user.employee:
        entity_dict = user.employee.to_dict()
    if user.secretary:
        entity_dict = user.secretary.to_dict()
    user_dict = user.to_dict(exclude=EXCLUDE_CREATE)
    entity_dict.update(user_dict)

    return entity_dict


def admin_to_dict(admin, exclude_type):
    user = admin.user
    admin_dict = admin.to_dict()
    user_dict = user.to_dict(exclude=exclude_type)
    admin_dict.update(user_dict)

    return admin_dict


def driver_to_dict(driver, exclude_type):
    user = driver.user
    driver_dict = driver.to_dict()
    user_dict = user.to_dict(exclude=exclude_type)
    driver_dict.update(user_dict)
    reservation_list = []
    for reservation in driver.reservations.all():
        reservation_list.append(reservation.to_dict())
    driver_dict["reservations"] = reservation_list

    return driver_dict


def employee_to_dict(employee, exclude_type):
    user = employee.user
    employee_dict = employee.to_dict()
    user_dict = user.to_dict(exclude=exclude_type)
    employee_dict.update(user_dict)

    return employee_dict


def secretary_to_dict(secretary, exclude_type):
    user = secretary.user
    secretary_dict = secretary.to_dict()
    user_dict = user.to_dict(exclude=exclude_type)
    secretary_dict.update(user_dict)

    return secretary_dict
