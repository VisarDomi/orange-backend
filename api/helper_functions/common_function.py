from flask import g


def apply_role_to_dict(user, user_dict):
    role = "unassigned"
    role_id = "no_id"
    if user.admin:
        role = "admin"
        role_id = user.admin.id
    if user.driver:
        role = "driver"
        role_id = user.driver.id
    if user.company:
        role = "company"
        role_id = user.company.id
    if user.employee:
        role = "employee"
        role_id = user.employee.id
    user_dict["role"] = role
    user_dict["role_id"] = role_id

    return user_dict


def can_it_update(employee_id=0, company_id=0, driver_id=0, admin_id=0):
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
        is_admin = int(admin_id) == g.current_user.admin.id
    if is_company or is_employee or is_driver or is_admin:
        can_update = True

    return can_update
