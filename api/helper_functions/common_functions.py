from .get_by_id import get_user_by_id
from .constants import UNASSIGNED
from flask import g
from ..common.exceptions import NotCorrectRole


def apply_role_check(login_data, user_dict):
    if login_data["role"] == UNASSIGNED:
        msg = "The user does not have a role, cannot proceed login"
        raise NotCorrectRole(message=msg)
    if login_data["role"] != user_dict["role"]:
        msg = "This is not the correct role of the user, cannot proceed login"
        raise NotCorrectRole(message=msg)


def can_it_update(employee_id=0, company_id=0, driver_id=0):
    is_admin = False
    is_company = False
    is_driver = False
    is_employee = False
    can_update = False
    if g.current_user.admin:
        is_admin = True
    if g.current_user.company:
        is_company = int(company_id) == g.current_user.company.id
    if g.current_user.driver:
        is_driver = int(driver_id) == g.current_user.driver.id
    if g.current_user.employee:
        is_employee = int(employee_id) == g.current_user.employee.id
    if is_admin or is_company or is_driver or is_employee:
        can_update = True

    return can_update


def is_it_duplicate_role(user_id):
    has_role = False
    counter = 0
    user = get_user_by_id(user_id)
    if user.admin:
        counter += 1
    if user.company:
        counter += 1
    if user.employee:
        counter += 1
    if user.driver:
        counter += 1
    if counter > 0:
        has_role = True

    return has_role
