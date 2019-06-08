from flask import request
from ..common.validation import schema
from ..bp_auth.views import token_auth
from . import bp
from . import domain


@bp.route("", methods=["POST"])
@schema("create_stop.json")
@token_auth.login_required
def create_stop():
    return domain.create_stop(request.json)


@bp.route("/all", methods=["GET"])
@token_auth.login_required
def get_stops():

    return domain.get_stops()


@bp.route("/<stop_id>", methods=["GET"])
@token_auth.login_required
def get_stop(stop_id):

    return domain.get_stop(stop_id)


# order is route, schema, auth
@bp.route("/<stop_id>", methods=["PUT"])
@schema("/update_stop.json")
@token_auth.login_required
def update_stop(stop_id):

    return domain.update_stop(request.json, stop_id)


@bp.route("/<stop_id>", methods=["DELETE"])
@token_auth.login_required
def delete_stop(stop_id):
    domain.delete_stop(stop_id)

    return {"message": "Stop with `id: %s` has been deleted." % stop_id}
