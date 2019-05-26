from sqlalchemy.orm.exc import NoResultFound
from ..common.exceptions import RecordNotFound, InvalidURL
from ..common.models import User


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
