EXPIRES_IN = 360_000_000


def get_entity(entity_id, Entity):
    entity = Entity.query.filter(Entity.id == int(entity_id)).one()

    return entity


def get_user_by_id(user_id):
    user = get_entity(user_id, User)

    return user


def create_user(user_data):
    user_data["email"] = user_data["email"].lower()
    user = User(**user_data)
    user.set_password(user_data["password"])
    user.save()
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


user_data = {"email": "admin@orange-backend.ml", "password": "password"}
user = create_user(user_data)
user_id = user.id
print("user is:", user)

admin_data = {"full_name": "Administrator", "user_id": user_id}

admin = create_admin(admin_data)
print("admin is:", admin)


db_session.commit()
