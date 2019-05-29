from ..helper_functions.constants import ONLY, EXCLUDE
from ..helper_functions.common_function import apply_role_to_dict
from . import backend


def create_user(user_data):
    user = backend.create_user(user_data)
    user_dict = user.to_dict(exclude=EXCLUDE)
    user_dict = apply_role_to_dict(user, user_dict)

    return user_dict


def get_user_by_id(user_id):
    user = backend.get_user(user_id)
    user_dict = user.to_dict(only=ONLY)
    user_dict = apply_role_to_dict(user, user_dict)

    return user_dict


def get_all_users():
    users = backend.get_all_users()
    users_list = []
    for user in users:
        user_dict = user.to_dict(only=ONLY)
        user_dict = apply_role_to_dict(user, user_dict)
        users_list.append(user_dict)

    return users_list


def update_user(user_data, user_id):
    user = backend.update_user(user_data, user_id)
    user_dict = user.to_dict(only=ONLY)
    user_dict = apply_role_to_dict(user, user_dict)

    return user_dict


def delete_user(user_id):
    backend.delete_user(user_id)
