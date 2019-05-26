from . import bp
from . import domain
from ..bp_auth.views import token_auth


@bp.route("/<user_id>", methods=["GET"])
@token_auth.login_required
def get_user(user_id):
    return domain.get_user_by_id(user_id)
