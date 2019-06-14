from sqlalchemy.orm.exc import NoResultFound
from ..common.exceptions import (
    RecordNotFound,
    InvalidURL,
    CannotGetOthersData,
    RecordAlreadyExists,
    MissingArguments,
)
from ..models.users import User, Admin, Driver, Employee, Secretary
from ..models.items import (
    Company,
    Reservation,
    Invoice,
    Item,
    Itinerary,
    ItineraryMaster,
    Stop,
)
from .constants import (
    EXPIRES_IN,
    ENTITY_NAME,
    USER_NAME,
    ADMIN_NAME,
    DRIVER_NAME,
    EMPLOYEE_NAME,
    SECRETARY_NAME,
    COMPANY_NAME,
    RESERVATION_NAME,
    INVOICE_NAME,
    ITEM_NAME,
    ITINERARY_NAME,
    ITINERARY_MASTER_NAME,
    STOP_NAME,
)


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
        msg = "Email `%s` is already in use for another account." % user_data["email"]
        raise RecordAlreadyExists(message=msg)
    user.get_token(expires_in=EXPIRES_IN)

    return user


def create_entity(entity_data, Entity):
    user_data = entity_data.pop("user")
    user = create_user(user_data)
    entity = Entity(**entity_data)
    entity.user = user
    entity.save()

    return entity


def get_entity_name(Entity):
    entity_name = ENTITY_NAME
    if Entity == User:
        entity_name = USER_NAME
    if Entity == Admin:
        entity_name = ADMIN_NAME
    if Entity == Driver:
        entity_name = DRIVER_NAME
    if Entity == Employee:
        entity_name = EMPLOYEE_NAME
    if Entity == Secretary:
        entity_name = SECRETARY_NAME
    if Entity == Company:
        entity_name = COMPANY_NAME
    if Entity == Reservation:
        entity_name = RESERVATION_NAME
    if Entity == Invoice:
        entity_name = INVOICE_NAME
    if Entity == Item:
        entity_name = ITEM_NAME
    if Entity == Itinerary:
        entity_name = ITINERARY_NAME
    if Entity == ItineraryMaster:
        entity_name = ITINERARY_MASTER_NAME
    if Entity == Stop:
        entity_name = STOP_NAME

    return entity_name


def get_entity(entity_id, Entity):
    entity_name = get_entity_name(Entity)
    try:
        entity = Entity.query.filter(Entity.id == int(entity_id)).one()
    except NoResultFound:
        if int(entity_id) == 0:
            msg = f"You don't have permissions."
            status_code = 403
            raise CannotGetOthersData(message=msg, status_code=status_code)
        else:
            msg = f"There is no {entity_name} with id {entity_id}."
            raise RecordNotFound(message=msg)
    except (InvalidURL, ValueError):
        msg = f"This is not a valid URL: {entity_id}`"
        raise InvalidURL(message=msg)

    return entity
