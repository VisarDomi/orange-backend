from flask import g, request
from flask_httpauth import HTTPBasicAuth
from flask_httpauth import HTTPTokenAuth
from ..models.users import User
from ..helper_functions.constants import EXCLUDE, EXPIRES_IN
from ..helper_functions.common_functions import apply_role_to_dict
from . import bp
from ..common.exceptions import NotCorrectRole


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

    return {
        "error message": "You are not logged in or bad login "
        "username/password combo. (@basic_auth.error_handler)"
    }


@bp.route("/login", methods=["POST"])
@basic_auth.login_required
def login():
    g.current_user.get_token(expires_in=EXPIRES_IN)
    user = g.current_user
    user_dict = user.to_dict(exclude=EXCLUDE)
    user_dict = apply_role_to_dict(user, user_dict)
    login_data = request.json
    if login_data["role"] != user_dict["role"]:
        msg = "This is not the correct role, cannot proceed login"
        raise NotCorrectRole(message=msg)
    if user_dict["role"] == "admin":
        user_dict["full_name"] = user.admin.full_name
    if user_dict["role"] == "company":
        user_dict["full_name"] = user.company.full_name
    if user_dict["role"] == "employee":
        user_dict["full_name"] = user.employee.full_name
    if user_dict["role"] == "driver":
        user_dict["full_name"] = user.driver.full_name

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
