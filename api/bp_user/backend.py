from flask import g
from ..common.exceptions import (
    RecordAlreadyExists,
    MissingArguments,
    CannotChangeOthersData,
    CannotDeleteOthersData,
    CannotDeleteFirstAdmin,
)
from ..common.models import User
from ..helper_functions.get_by_id import get_user_by_id


def create_user(user_data):
    if user_data["email"] is None or user_data["password"] is None:
        msg = "Please provide an email and a password."
        raise MissingArguments(message=msg)
    if not User.query.filter(User.email == user_data["email"]).one_or_none():
        user_data["email"] = user_data["email"].lower()
        user = User(**user_data)
        user.set_password(user_data["password"])
        user.save()
    else:
        msg = "Email `%s` is already in use for another account." % user_data["email"]
        raise RecordAlreadyExists(message=msg)
    if user.id == 1:
        user.role = "admin"
        user.save()
    user.get_token(expires_in=36_000_000)

    return user


def get_all_users():
    users = User.query.all()

    return users


def update_user(user_data, user_id):
    if int(user_id) == g.current_user.id:
        user = get_user_by_id(user_id)
        user.update(**user_data)
        user.save()

    else:
        msg = "You can't change other people's data."
        raise CannotChangeOthersData(message=msg)

    return user


def delete_user(user_id):
    if int(user_id) != 1:
        if int(user_id) == g.current_user.id:
            user = get_user_by_id(user_id)
            user.delete()
        else:
            msg = "You can't delete other people's data."
            raise CannotDeleteOthersData(message=msg)
    else:
        msg = "Cannot delete admin with `id: %s`" % user_id
        raise CannotDeleteFirstAdmin(message=msg)
