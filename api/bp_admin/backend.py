from ..common.exceptions import CannotChangeFirstAdminProperties
from ..helper_functions.decorators import admin_required
from ..helper_functions.get_by_id import get_user_by_id


def get_and_update_user(user_data, user_id):
    user = get_user_by_id(user_id)
    user.update(**user_data)
    user.save()

    return user


@admin_required
def update_user(user_data, user_id):

    secure = True
    if secure:
        if int(user_id) != 1:
            user = get_and_update_user(user_data, user_id)
        else:
            msg = "Cannot change admin with `id: %s`" % user_id
            raise CannotChangeFirstAdminProperties(message=msg)
    else:
        user = get_and_update_user(user_data, user_id)

    return user
