from flask import g
from ..common.exceptions import CannotChangeOthersData, CannotDeleteOthersData
from ..common.models import Employee
from ..helper_functions.create import create_entity
from ..helper_functions.get_by_id import get_employee_by_id, get_company_by_id


def create_employee(employee_data, company_id):
    employee = create_entity(employee_data, Employee)
    company = get_company_by_id(company_id)
    employee.company = company
    employee.save()

    return employee


def get_all_employees(company_id):
    company = get_company_by_id(company_id)
    employees = company.employees.all()

    return employees


def update_employee(employee_data, employee_id, company_id):
    try:
        is_employee = int(employee_id) == g.current_user.employee.id
        is_company = int(company_id) == g.current_user.company.id
        print("is_employee, is_company :", is_employee, is_company)
        if is_employee or is_company:
            employee = get_employee_by_id(employee_id)
            employee.update(**employee_data)
            employee.save()
        else:
            msg = "You can't change other people's data."
            raise CannotChangeOthersData(message=msg)
    except AttributeError:
        msg = "AttributeError, You can't change other people's data."
        raise CannotChangeOthersData(message=msg)

    return employee


def delete_employee(employee_id, company_id):
    try:
        if int(employee_id) == g.current_user.id:
            employee = get_employee_by_id(employee_id)
            employee.delete()
        else:
            msg = "You can't delete other people's data."
            raise CannotDeleteOthersData(message=msg)
    except AttributeError:
        msg = "AttributeError, You can't change other people's data."
        raise CannotChangeOthersData(message=msg)
