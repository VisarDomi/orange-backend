from ..helper_functions.get_by_id import get_employee_by_id as backend_get_employee_by_id
from . import backend


def create_employee(employee_data):
    employee = backend.create_employee(employee_data)
    employee_dict = employee.to_dict()

    return employee_dict


def get_employee_by_id(employee_id):
    employee = backend_get_employee_by_id(employee_id)
    employee_dict = employee.to_dict()

    return employee_dict


def get_all_employees():
    employees = backend.get_all_employees()
    employees_list = []
    for employee in employees:
        employee_dict = employee.to_dict()
        employees_list.append(employee_dict)

    return employees_list


def update_employee(employee_data, employee_id):
    employee = backend.update_employee(employee_data, employee_id)
    employee_dict = employee.to_dict()

    return employee_dict


def delete_employee(employee_id):
    backend.delete_employee(employee_id)
