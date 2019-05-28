from flask import g
from ..common.exceptions import (
    CannotChangeOthersData,
    CannotDeleteOthersData,
)
from ..common.models import Admin
from ..helper_functions.get_by_id import get_admin_by_id


def create_admin(admin_data):
    admin = Admin(**admin_data)
    admin.save()

    return admin


def get_all_admins():
    admins = Admin.query.all()

    return admins


def update_admin(admin_data, admin_id):
    if int(admin_id) == g.current_user.id:
        admin = get_admin_by_id(admin_id)
        admin.update(**admin_data)
        admin.save()
    else:
        msg = "You can't change other people's data."
        raise CannotChangeOthersData(message=msg)

    return admin


def delete_admin(admin_id):
    if int(admin_id) == g.current_user.id:
        admin = get_admin_by_id(admin_id)
        admin.delete()
    else:
        msg = "You can't delete other people's data."
        raise CannotDeleteOthersData(message=msg)
