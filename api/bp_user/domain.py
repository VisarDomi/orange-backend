from ..helper_functions.get_by_id import get_user_by_id as backend_get_user_by_id
from ..helper_functions.constants import ONLY, EXCLUDE
from ..helper_functions.common_function import apply_role
from . import backend


def create_user(user_data):
    user = backend.create_user(user_data)
    user_dict = user.to_dict(exclude=EXCLUDE)

    return user_dict


def get_user_by_id(user_id):
    user = backend_get_user_by_id(user_id)
    user_dict = user.to_dict(only=ONLY)
    role = apply_role(user)
    user_dict["role"] = role

    return user_dict


def get_all_users():
    users = backend.get_all_users()
    users_list = []
    for user in users:
        user_dict = user.to_dict(only=ONLY)
        role = apply_role(user)
        user_dict["role"] = role
        users_list.append(user_dict)

    return users_list


def update_user(user_data, user_id):
    user = backend.update_user(user_data, user_id)
    user_dict = user.to_dict(only=ONLY)

    return user_dict


def delete_user(user_id):
    backend.delete_user(user_id)
