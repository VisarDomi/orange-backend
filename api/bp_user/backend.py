from flask import g
from ..common.exceptions import (
    RecordAlreadyExists,
    MissingArguments,
    CannotChangeOthersData,
    CannotDeleteOthersData,
)
from ..models.users import User
from ..helper_functions.get_by_id import get_user_by_id
from ..helper_functions.constants import EXPIRES_IN
from ..helper_functions.common_functions import can_it_update


def create_user(user_data):
    if user_data["email"] is None or user_data["password"] is None:
        msg = "Please provide a email and a password."
        raise MissingArguments(message=msg)
    if not User.query.filter(User.email == user_data["email"]).one_or_none():
        user_data["email"] = user_data["email"].lower()
        user = User(**user_data)
        user.set_password(user_data["password"])
        user.save()
    else:
        msg = "Login `%s` is already in use for another account." % user_data["email"]
        raise RecordAlreadyExists(message=msg)
    user.get_token(expires_in=EXPIRES_IN)

    return user


def get_users():
    users = User.query.all()

    return users


def get_user(user_id):
    user = get_user_by_id(user_id)

    return user


def update_user(user_data, user_id):
    can_update = can_it_update()
    is_current_user = int(user_id) == g.current_user.id
    if is_current_user or can_update:
        user = get_user_by_id(user_id)
        user.update(**user_data)
        user.save()

    else:
        msg = "You can't change other people's data."
        raise CannotChangeOthersData(message=msg)

    return user


def delete_user(user_id):
    can_update = can_it_update()
    is_current_user = int(user_id) == g.current_user.id
    if is_current_user or can_update:
        user = get_user_by_id(user_id)
        user.delete()
    else:
        msg = "You can't delete other people's data."
        raise CannotDeleteOthersData(message=msg)
