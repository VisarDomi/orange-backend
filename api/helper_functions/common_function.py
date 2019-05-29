from ..common.exceptions import CannotHaveMultipleRoles


def apply_role_to_dict(user, user_dict):
    role = "unassigned"
    counter = 0
    if user.admin:
        role = "admin"
        counter += 1
    if user.driver:
        role = "driver"
        counter += 1
    if user.company:
        role = "company"
        counter += 1
    if user.employee:
        role = "employee"
        counter += 1
    user_dict["role"] = role
    if counter > 1:
        msg = "There are multiple roles for this user which is not allowed"
        raise CannotHaveMultipleRoles(message=msg)

    return user_dict
