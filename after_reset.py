from sqlalchemy.orm.exc import NoResultFound
from api.common.exceptions import RecordNotFound, InvalidURL
from api.common.exceptions import (
    RecordAlreadyExists,
    MissingArguments,
)
from api.common.models import (
    User,
    Admin,
    # Driver,
    # Employee,
    # Company,
    # Reservation,
    # Invoice,
    # Item,
)
EXPIRES_IN = 360_000_000


def get_entity(entity_id, Entity):
    try:
        entity = Entity.query.filter(Entity.id == int(entity_id)).one()
    except NoResultFound:
        msg = f"There is no entity with id {entity_id}"
        raise RecordNotFound(message=msg)
    except (InvalidURL, ValueError):
        msg = f"This is not a valid URL: {entity_id}`"
        raise InvalidURL(message=msg)

    return entity


def get_user_by_id(user_id):
    user = get_entity(user_id, User)

    return user


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


def create_entity(entity_data, Entity):
    user_id = entity_data.pop("user_id")
    user = get_user_by_id(user_id)
    entity = Entity(**entity_data)
    entity.user = user
    entity.save()

    return entity


def create_admin(admin_data):
    admin = create_entity(admin_data, Admin)

    return admin


user_data = {
    "email": "admin@orange-backend.ml",
    "password": "password"
}
user = create_user(user_data)
user_id = user.id
print("user is:", user)

admin_data = {
    "full_name": "Administrator",
    "user_id": user_id
}

admin = create_admin(admin_data)
print("admin is:", admin)
