from flask import g
from functools import wraps
from ..common.exceptions import YouAreNotAdmin, CannotChangeOthersData
from .common_function import can_it_update


def admin_required(a_function):
    @wraps(a_function)
    def decorated_function(*args, **kwargs):
        if g.current_user.admin:
            return a_function(*args, **kwargs)  # here goes the function
        else:
            msg = "You are not an admin."
            raise YouAreNotAdmin(message=msg)

    return decorated_function


def can_make_reservation(employee_id=0, company_id=0, driver_id=0):
    def real_decorator(a_function):
        @wraps(a_function)
        def decorated_function(*args, **kwargs):
            can_update = can_it_update(employee_id, company_id, driver_id)
            if can_update:
                return a_function(*args, **kwargs)  # here goes the function
            else:
                msg = "You can't change other people's data."
                raise CannotChangeOthersData(message=msg)

        return decorated_function
    return real_decorator
