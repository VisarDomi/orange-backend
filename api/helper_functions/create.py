from ..common.exceptions import DuplicateRole
from .get_by_id import get_user_by_id
from .common_functions import is_it_duplicate_role


def create_entity(entity_data, Entity):
    user_id = entity_data.pop("user_id")
    has_role = is_it_duplicate_role(user_id)
    if has_role:
        msg = "This user already has a role, cannot assign another role."
        raise DuplicateRole(message=msg)
    entity = Entity(**entity_data)
    user = get_user_by_id(user_id)
    entity.user = user
    entity.save()

    return entity
