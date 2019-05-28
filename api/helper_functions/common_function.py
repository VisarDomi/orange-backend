def apply_role(user):
    role = "unassigned"
    if user.admin:
        role = "admin"
    if user.driver:
        role = "driver"
    if user.company:
        role = "company"
    if user.employee:
        role = "employee"

    return role
