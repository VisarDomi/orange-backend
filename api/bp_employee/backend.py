from flask import g
from ..common.exceptions import (
    CannotChangeOthersData,
    CannotDeleteOthersData,
)
from ..common.models import Employee
from ..helper_functions.get_by_id import get_employee_by_id


def create_employee(employee_data):
    employee = Employee(**employee_data)
    employee.save()

    return employee


def get_all_employees():
    employees = Employee.query.all()

    return employees


def update_employee(employee_data, employee_id):
    if int(employee_id) == g.current_user.id:
        employee = get_employee_by_id(employee_id)
        employee.update(**employee_data)
        employee.save()
    else:
        msg = "You can't change other people's data."
        raise CannotChangeOthersData(message=msg)

    return employee


def delete_employee(employee_id):
    if int(employee_id) == g.current_user.id:
        employee = get_employee_by_id(employee_id)
        employee.delete()
    else:
        msg = "You can't delete other people's data."
        raise CannotDeleteOthersData(message=msg)
