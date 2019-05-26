from ..helper_functions.decorators import admin_required
from ..helper_functions.get_by_id import get_user_by_id as backend_get_user_by_id
from ..helper_functions.constants import ONLY


@admin_required
def get_user_by_id(user_id):
    user = backend_get_user_by_id(user_id)
    user_dict = user.to_dict(only=ONLY)

    return user_dict
