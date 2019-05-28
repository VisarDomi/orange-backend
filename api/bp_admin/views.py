from flask import request
from ..common.validation import schema
from ..bp_auth.views import token_auth
from . import bp
from . import domain


@bp.route("", methods=["POST"])
@schema("create_admin.json")
@token_auth.login_required
def create_admin():
    return domain.create_admin(request.json)


@bp.route("/<admin_id>", methods=["GET"])
def get_admin(admin_id):

    return domain.get_admin_by_id(admin_id)


@bp.route("/all", methods=["GET"])
@token_auth.login_required
def get_admins():

    return domain.get_all_admins()


# order is route, schema, auth
@bp.route("/<admin_id>", methods=["PUT"])
@schema("/update_admin.json")
@token_auth.login_required
def update_admin(admin_id):

    return domain.update_admin(request.json, admin_id)


@bp.route("/<admin_id>", methods=["DELETE"])
@token_auth.login_required
def delete_admin(admin_id):
    domain.delete_admin(admin_id)

    return {"message": "Admin with `id: %s` has been deleted." % admin_id}


@bp.route("/role", methods=["POST"])
@schema("change_role.json")
@token_auth.login_required
def change_role():
    return domain.change_role(request.json)
