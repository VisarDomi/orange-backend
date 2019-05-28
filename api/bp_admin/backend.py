from flask import g
from ..common.exceptions import (
    MissingArguments,
    CannotChangeOthersData,
    CannotDeleteOthersData,
)
from ..common.models import Admin
from ..helper_functions.get_by_id import (
    get_admin_by_id,
    get_user_by_id,
    get_driver_by_id,
)
from ..helper_functions.decorators import admin_required


@admin_required
def create_admin(admin_data):
    admin = Admin(**admin_data)
    admin.save()

    return admin


def get_all_admins():
    admins = Admin.query.all()

    return admins


@admin_required
def update_admin(admin_data, admin_id):
    if int(admin_id) == g.user.current_user.id:
        admin = get_admin_by_id(admin_id)
        admin.update(**admin_data)
        admin.save()
    else:
        msg = "You can't change other people's data."
        raise CannotChangeOthersData(message=msg)

    return admin


@admin_required
def delete_admin(admin_id):
    if int(admin_id) == g.user.current_user.id:
        admin = get_admin_by_id(admin_id)
        admin.delete()
    else:
        msg = "You can't delete other people's data."
        raise CannotDeleteOthersData(message=msg)


@admin_required
def change_role(role_data):
    user_id = role_data["user_id"]
    if not user_id:
        msg = "Please provide a user_id you want to change it's role."
        raise MissingArguments(message=msg)
    user = get_user_by_id(user_id)
    counter = 0
    try:
        admin_id = role_data["admin_id"]
        if admin_id:
            admin = get_admin_by_id(admin_id)
            user.admin = admin
        else:
            counter += 1
    except IndexError:
        counter += 1
    try:
        driver_id = role_data["driver_id"]
        if driver_id:
            driver = get_driver_by_id(driver_id)
            user.driver = driver
        else:
            counter += 1
    except IndexError:
        counter += 1
    if counter == 2:
        msg = "Please provide a admin_id or driver_id that you want to change the user's role."
        raise MissingArguments(message=msg)

    return user
