from ..common.exceptions import (
    MissingArguments,
    CannotChangeOthersData,
    CannotDeleteOthersData,
)
from ..common.models import Admin
from ..helper_functions.create import create_entity
from ..helper_functions.get_by_id import (
    get_admin_by_id,
    get_user_by_id,
    get_driver_by_id,
    get_company_by_id,
    get_employee_by_id,
)
from ..helper_functions.decorators import admin_required
from ..helper_functions.common_function import can_it_update


@admin_required
def create_admin(admin_data):
    admin = create_entity(admin_data, Admin)

    return admin


def get_all_admins():
    admins = Admin.query.all()

    return admins


@admin_required
def update_admin(admin_data, admin_id):
    can_update = can_it_update()
    if can_update:
        admin = get_admin_by_id(admin_id)
        admin.update(**admin_data)
        admin.save()
    else:
        msg = "You can't change other people's data."
        raise CannotChangeOthersData(message=msg)

    return admin


@admin_required
def delete_admin(admin_id):
    can_update = can_it_update()
    if can_update:
        admin = get_admin_by_id(admin_id)
        admin.delete()
    else:
        msg = "You can't delete other people's data."
        raise CannotDeleteOthersData(message=msg)


# dev only
@admin_required
def change_role(role_data):
    user_id = role_data["user_id"]
    if not user_id:
        msg = "Please provide a user_id you want to change it's role."
        raise MissingArguments(message=msg)
    user = get_user_by_id(user_id)

    # comment the following block to add/remove the "without a role" restriction
    # if user.admin or user.driver or user.company or user.company:
    #     msg = "Please provide a user without a role."
    #     raise MissingArguments(message=msg)

    counter_error = 0
    max_role = 0
    try:
        admin_id = role_data["admin_id"]
        if admin_id:
            admin = get_admin_by_id(admin_id)
            user.admin = admin
            max_role += 1
        else:
            counter_error += 1
    except IndexError:
        counter_error += 1
    try:
        driver_id = role_data["driver_id"]
        if driver_id:
            driver = get_driver_by_id(driver_id)
            user.driver = driver
            max_role += 1
        else:
            counter_error += 1
    except IndexError:
        counter_error += 1
    try:
        company_id = role_data["company_id"]
        if company_id:
            company = get_company_by_id(company_id)
            user.company = company
            max_role += 1
        else:
            counter_error += 1
    except IndexError:
        counter_error += 1
    try:
        employee_id = role_data["employee_id"]
        if employee_id:
            employee = get_employee_by_id(employee_id)
            user.employee = employee
            max_role += 1
        else:
            counter_error += 1
    except IndexError:
        counter_error += 1
    if counter_error > 3 and max_role > 1:
        msg = "Please provide exactly one role id."
        raise MissingArguments(message=msg)

    return user
