from . import backend


def get_reservations(driver_id):
    reservations = backend.get_reservations(driver_id)
    reservations_list = []
    for reservation in reservations:
        reservation_dict = reservation.to_dict()
        employees = []
        for employee in reservation.employees.all():
            employees.append(employee.to_dict())
        reservation_dict["employees"] = employees
        reservations_list.append(reservation_dict)

    return reservations_list


def get_reservation(driver_id, reservation_id):
    reservation = backend.get_reservation(driver_id, reservation_id)
    reservation_dict = reservation.to_dict()
    employees = []
    for employee in reservation.employees.all():
        employees.append(employee.to_dict())
    reservation_dict["employees"] = employees

    return reservation_dict


def update_reservation(reservation_data, driver_id, reservation_id):
    reservation = backend.update_reservation(
        reservation_data, driver_id, reservation_id
    )
    reservation_dict = reservation.to_dict()
    employees = []
    for employee in reservation.employees.all():
        employees.append(employee.to_dict())
    reservation_dict["employees"] = employees

    return reservation_dict
