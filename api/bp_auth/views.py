from flask import g, request
from flask_httpauth import HTTPBasicAuth
from flask_httpauth import HTTPTokenAuth
from ..common.exceptions import BadLogin
from ..models.users import User
from ..helper_functions.constants import EXPIRES_IN, EXCLUDE
from ..helper_functions.dict import user_to_dict
from ..helper_functions.common_functions import apply_role_check
from . import bp


basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()


@basic_auth.verify_password
def verify_password(email, password):
    user = User.query.filter_by(email=email.lower()).first()
    if user is None:
        return False
    g.current_user = user

    return user.check_password(password)


@basic_auth.error_handler
def basic_auth_error():
    msg = (
        "You are not logged in or bad login "
        "username/password combo. (@basic_auth.error_handler)"
    )
    raise BadLogin(message=msg, status_code=401)

    return {
        "error message": "You are not logged in or bad login "
        "username/password combo. (@basic_auth.error_handler)"
    }


@bp.route("/login", methods=["POST"])
@basic_auth.login_required
def login():
    g.current_user.get_token(expires_in=EXPIRES_IN)
    user = g.current_user
    user_dict = user_to_dict(user, EXCLUDE)
    login_data = request.json
    apply_role_check(login_data, user_dict)

    return user_dict


@token_auth.verify_token
def verify_token(token):
    g.current_user = User.check_token(token) if token else None

    return g.current_user is not None


@token_auth.error_handler
def token_auth_error():

    return {
        "error message": "You sent the wrong token or no "
        "token at all. (@token_auth.error_handler)"
    }
