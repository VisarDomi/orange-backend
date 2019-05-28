from ..helper_functions.get_by_id import get_admin_by_id as backend_get_admin_by_id
from ..helper_functions.constants import ONLY
from . import backend


def create_admin(admin_data):
    admin = backend.create_admin(admin_data)
    admin_dict = admin.to_dict()

    return admin_dict


def get_admin_by_id(admin_id):
    admin = backend_get_admin_by_id(admin_id)
    admin_dict = admin.to_dict()

    return admin_dict


def get_all_admins():
    admins = backend.get_all_admins()
    admins_list = []
    for admin in admins:
        admin_dict = admin.to_dict()
        admins_list.append(admin_dict)

    return admins_list


def update_admin(admin_data, admin_id):
    admin = backend.update_admin(admin_data, admin_id)
    admin_dict = admin.to_dict()

    return admin_dict


def delete_admin(admin_id):
    backend.delete_admin(admin_id)


def change_role(role_data):
    user = backend.change_role(role_data)
    user_dict = user.to_dict(only=ONLY)

    return user_dict
