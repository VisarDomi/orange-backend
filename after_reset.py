# cp in flask shell after 'alembic upgrade head' after 'drop database orange'
from api.helper_functions.constants import EXPIRES_IN, EXCLUDE_CREATE
from api.helper_functions.users_to_dict import admin_to_dict

import pprint
pp = pprint.PrettyPrinter(indent=4)


def create_user(user_data):
    user_data["email"] = user_data["email"].lower()
    user = User(**user_data)
    user.set_password(user_data["password"])
    user.save()
    user.get_token(expires_in=EXPIRES_IN)

    return user


def create_entity(entity_data, Entity):
    user_data = entity_data.pop("user")
    user = create_user(user_data)
    entity = Entity(**entity_data)
    entity.user = user
    entity.save()

    return entity


admin_data = {
    "full_name": "Administrator",
    "user": {"email": "admin@orange.com", "password": "password"},
}
admin = create_entity(admin_data, Admin)
admin_dict = admin_to_dict(admin, EXCLUDE_CREATE)
print("created admin is:")
pp.pprint(admin_dict)
db_session.commit()
