from ..helper_functions.constants import ONLY, EXCLUDE
from ..helper_functions.dict import user_to_dict
from . import backend


def create_user(user_data):
    user = backend.create_user(user_data)
    user_dict = user_to_dict(user, EXCLUDE)

    return user_dict


def get_users():
    users = backend.get_users()
    users_list = []
    for user in users:
        user_dict = user_to_dict(user, ONLY)
        users_list.append(user_dict)

    return users_list


def get_user(user_id):
    user = backend.get_user(user_id)
    user_dict = user_to_dict(user, ONLY)

    return user_dict


def update_user(user_data, user_id):
    user = backend.update_user(user_data, user_id)
    user_dict = user_to_dict(user, ONLY)

    return user_dict


def delete_user(user_id):
    backend.delete_user(user_id)
