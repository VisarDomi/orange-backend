from flask import g
from ..common.exceptions import CannotHaveMultipleRoles
from ..common.models import Admin


def apply_role_to_dict(user, user_dict):
    role = "unassigned"
    counter = 0
    if user.admin:
        role = "admin"
        counter += 1
    if user.driver:
        role = "driver"
        counter += 1
    if user.company:
        role = "company"
        counter += 1
    if user.employee:
        role = "employee"
        counter += 1
    user_dict["role"] = role
    if counter > 1:
        msg = "There are multiple roles for this user which is not allowed"
        raise CannotHaveMultipleRoles(message=msg)

    return user_dict


def is_it_admin():
    is_admin = False
    admins = Admin.query.all()
    for admin in admins:
        if admin == g.current_user.admin:
            is_admin = True
    return is_admin


def can_it_update(employee_id=0, company_id=0, driver_id=0):
    is_employee = False
    is_company = False
    is_driver = False
    is_admin = False
    can_update = False
    if g.current_user.employee:
        is_employee = int(employee_id) == g.current_user.employee.id
    if g.current_user.company:
        is_company = int(company_id) == g.current_user.company.id
    if g.current_user.driver:
        is_driver = int(driver_id) == g.current_user.driver.id
    if g.current_user.admin:
        is_admin = is_it_admin()
    if is_company or is_employee or is_driver or is_admin:
        can_update = True

    return can_update
