from . import backend


def create_reservation(reservation_data, company_id):
    reservation = backend.create_reservation(reservation_data, company_id)
    reservation_dict = reservation.to_dict()
    employees = []
    for employee in reservation.employees.all():
        employees.append(employee.to_dict())
    if reservation.company:
        reservation_dict["company"] = reservation.company.to_dict()
    else:
        reservation_dict["company"] = {}
    if reservation.driver:
        reservation_dict["driver"] = reservation.driver.to_dict()
    else:
        reservation_dict["driver"] = {}
    reservation_dict["employees"] = employees

    return reservation_dict


def get_reservations(company_id):
    reservations = backend.get_reservations(company_id)
    reservations_list = []
    for reservation in reservations:
        reservation_dict = reservation.to_dict()
        employees = []
        for employee in reservation.employees.all():
            employees.append(employee.to_dict())
        if reservation.company:
            reservation_dict["company"] = reservation.company.to_dict()
        else:
            reservation_dict["company"] = {}
        if reservation.driver:
            reservation_dict["driver"] = reservation.driver.to_dict()
        else:
            reservation_dict["driver"] = {}
        reservation_dict["employees"] = employees
        reservations_list.append(reservation_dict)

    return reservations_list


def get_reservation(reservation_id, company_id):
    reservation = backend.get_reservation(reservation_id, company_id)
    reservation_dict = reservation.to_dict()
    employees = []
    for employee in reservation.employees.all():
        employees.append(employee.to_dict())
    if reservation.company:
        reservation_dict["company"] = reservation.company.to_dict()
    else:
        reservation_dict["company"] = {}
    if reservation.driver:
        reservation_dict["driver"] = reservation.driver.to_dict()
    else:
        reservation_dict["driver"] = {}
    reservation_dict["employees"] = employees

    return reservation_dict


def update_reservation(reservation_data, reservation_id, company_id):
    reservation = backend.update_reservation(
        reservation_data, reservation_id, company_id
    )
    reservation_dict = reservation.to_dict()
    employees = []
    for employee in reservation.employees.all():
        employees.append(employee.to_dict())
    if reservation.company:
        reservation_dict["company"] = reservation.company.to_dict()
    else:
        reservation_dict["company"] = {}
    if reservation.driver:
        reservation_dict["driver"] = reservation.driver.to_dict()
    else:
        reservation_dict["driver"] = {}
    reservation_dict["employees"] = employees

    return reservation_dict


def delete_reservation(reservation_id, company_id):
    backend.delete_reservation(reservation_id, company_id)
