from flask import g
from ..common.exceptions import NotCorrectRole
from .get_entity_by_id import get_company_by_id, get_secretary_by_id
from .constants import (
    UNASSIGNED,
    HEAD_SECRETARY,
    ADMIN,
    DRIVER,
    EMPLOYEE,
    SECRETARY,
)


def apply_role_check(login_data, user):
    role = None
    if user.admin:
        role = ADMIN
    if user.driver:
        role = DRIVER
    if user.employee:
        role = EMPLOYEE
    if user.secretary:
        role = SECRETARY
    if login_data["role"] == UNASSIGNED:
        msg = "The user does not have a role, cannot proceed login"
        raise NotCorrectRole(message=msg, status_code=403)
    if login_data["role"] != role:
        msg = "This is not the correct role of the user, cannot proceed login"
        raise NotCorrectRole(message=msg, status_code=403)


def can_it_update(employee_id=0, secretary_id=0, company_id=0, driver_id=0):
    is_admin = False
    is_driver = False
    is_employee = False
    is_secretary = False
    can_update = False
    if g.current_user.admin:
        is_admin = True
    if g.current_user.driver:
        is_driver = int(driver_id) == g.current_user.driver.id
    if g.current_user.employee:
        is_employee = int(employee_id) == g.current_user.employee.id
    if g.current_user.secretary:
        is_secretary = int(secretary_id) == g.current_user.secretary.id
    if is_admin or is_driver or is_employee or is_secretary:
        can_update = True

    return can_update


def get_secretary_id(company_id):
    secretary_id = 0
    company = get_company_by_id(company_id)
    secretarys = company.secretarys.all()
    for secretary in secretarys:
        if g.current_user.secretary == secretary:
            secretary_id = secretary.id

    return secretary_id


def is_it_head_secretary(company_id):
    is_head_secretary = False
    secretary_id = get_secretary_id(company_id)
    if g.current_user.secretary:
        secretary = get_secretary_by_id(secretary_id)
        if secretary.role == HEAD_SECRETARY:
            is_head_secretary = True

    return is_head_secretary
