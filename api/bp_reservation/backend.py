from ..common.exceptions import (
    CannotChangeOthersData,
    CannotDeleteOthersData,
    CannotCreateData,
    CannotGetOthersData,
)
from ..common.models import Reservation
from ..helper_functions.get_by_id import (
    get_employee_by_id,
    get_reservation_by_id,
    get_company_by_id,
)
from ..helper_functions.common_function import can_it_update


def create_reservation(reservation_data, company_id):
    can_update = can_it_update(company_id=company_id)
    if can_update:
        employee_ids = reservation_data.pop("employee_ids")
        reservation = Reservation(**reservation_data)
        company = get_company_by_id(company_id)
        reservation.company = company
        for employee_id in employee_ids:
            employee = get_employee_by_id(employee_id)
            reservation.employees.append(employee)
        reservation.save()
    else:
        msg = "You can't create data."
        raise CannotCreateData(message=msg)

    return reservation


def get_reservations(company_id):
    can_update = can_it_update(company_id=company_id)
    if can_update:
        company = get_company_by_id(company_id)
        reservations = company.reservations.all()
    else:
        msg = "You can't get reservations."
        raise CannotGetOthersData(message=msg)

    return reservations


def get_reservation(reservation_id, company_id):
    can_update = can_it_update(company_id=company_id)
    if can_update:
        reservation = get_reservation_by_id(reservation_id)
    else:
        msg = "You can't get reservation."
        raise CannotGetOthersData(message=msg)

    return reservation


def update_reservation(reservation_data, reservation_id, company_id):
    can_update = can_it_update(company_id=company_id)
    if can_update:
        employee_ids = reservation_data.pop("employee_ids")
        reservation = get_reservation_by_id(reservation_id)
        reservation.update(**reservation_data)
        for employee in reservation.employees.all():
            reservation.employees.remove(employee)
        for employee_id in employee_ids:
            employee = get_employee_by_id(employee_id)
            reservation.employees.append(employee)
        reservation.save()
    else:
        msg = "You can't change other people's data."
        raise CannotChangeOthersData(message=msg)

    return reservation


def delete_reservation(reservation_id, company_id):
    can_update = can_it_update(company_id=company_id)
    if can_update:
        reservation = get_reservation_by_id(reservation_id)
        reservation.delete()
    else:
        msg = "You can't delete other people's data."
        raise CannotDeleteOthersData(message=msg)
