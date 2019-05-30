from . import backend


def create_employee(employee_data, company_id):
    employee = backend.create_employee(employee_data, company_id)
    employee_dict = employee.to_dict()

    return employee_dict


def get_employees(company_id):
    employees = backend.get_employees(company_id)
    employees_list = []
    for employee in employees:
        employee_dict = employee.to_dict()
        employees_list.append(employee_dict)

    return employees_list


def get_employee(employee_id, company_id):
    employee = backend.get_employee(employee_id, company_id)
    employee_dict = employee.to_dict()

    return employee_dict


def update_employee(employee_data, employee_id, company_id):
    employee = backend.update_employee(employee_data, employee_id, company_id)
    employee_dict = employee.to_dict()

    return employee_dict


def delete_employee(employee_id, company_id):
    backend.delete_employee(employee_id, company_id)
