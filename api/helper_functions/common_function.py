def apply_role_to_dict(user, user_dict):
    role = "unassigned"
    if user.admin:
        role = "admin"
    if user.driver:
        role = "driver"
    if user.company:
        role = "company"
    if user.employee:
        role = "employee"
    user_dict["role"] = role

    return user_dict
