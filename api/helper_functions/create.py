from .get_by_id import get_user_by_id


def create_entity(entity_data, Entity):
    user_id = entity_data.pop("user_id")
    user = get_user_by_id(user_id)
    entity = Entity(**entity_data)
    entity.user = user
    entity.save()

    return entity
