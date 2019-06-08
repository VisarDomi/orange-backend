from ..common.exceptions import (
    CannotChangeOthersData,
    CannotDeleteOthersData,
    CannotCreateData,
    CannotGetOthersData,
)
from ..models.users import Employee
from ..helper_functions.create import create_entity
from ..helper_functions.get_by_id import (
    get_reservation_by_id,
    get_employee_by_id,
    get_company_by_id,
)
from ..helper_functions.common_functions import can_it_update


def create_employee(employee_data, company_id):
    can_update = can_it_update(company_id=company_id)
    if can_update:
        employee = create_entity(employee_data, Employee)
        company = get_company_by_id(company_id)
        employee.company = company
        employee.save()
    else:
        msg = "You can't create data."
        raise CannotCreateData(message=msg)

    return employee


def get_employees(company_id):
    company = get_company_by_id(company_id)
    employees = company.employees.all()

    return employees


def get_employee(employee_id, company_id):
    employee = get_employee_by_id(employee_id)

    return employee


def update_employee(employee_data, employee_id, company_id):
    can_update = can_it_update(employee_id=employee_id)
    if can_update:
        employee = get_employee_by_id(employee_id)
        employee.update(**employee_data)
        employee.save()
    else:
        msg = "You can't change other people's data."
        raise CannotChangeOthersData(message=msg)

    return employee


def delete_employee(employee_id, company_id):
    can_update = can_it_update(employee_id=employee_id)
    if can_update:
        employee = get_employee_by_id(employee_id)
        employee.delete()
    else:
        msg = "You can't delete other people's data."
        raise CannotDeleteOthersData(message=msg)


def get_reservations(employee_id, company_id):
    employee = get_employee_by_id(employee_id)
    stops = employee.stops.all()
    reservations = []
    for stop in stops:
        reservation = stop.reservation
        if reservation not in reservations:
            reservations.append(reservation)

    return reservations


def get_reservation(employee_id, company_id, reservation_id):
    reservation = get_reservation_by_id(reservation_id)

    return reservation
