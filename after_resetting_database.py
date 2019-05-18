#########################################################
# Admin
def create_user(user_data):
    if user_data["email"] is None or user_data["password"] is None:
        print("Please provide an email and a password.")
    if not User.query.filter(User.email == user_data["email"]).one_or_none():
        user = User(**user_data)
        user.set_password(user_data["password"])
        user.save()
    else:
        print(f'Email `{user_data["email"]}` is already in use for another account.')
    if user.id == 1:
        user.role = "admin"
        user.save()
    user.get_token(expires_in=36_000_000)

    return user

admin_dict = {
    "email": "admin@orange-backend.ml",
    "password": "password"
}
admin = create_user(admin_dict)
admin.save()


db_session.commit()
