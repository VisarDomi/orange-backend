from flask import request
from . import bp
from . import domain
from ..common.validation import schema
from ..bp_auth.views import token_auth


@bp.route("", methods=["POST"])
@schema("create_trip.json")
@token_auth.login_required
def create_trip(user_id):

    return domain.create_trip(request.json, user_id)


@bp.route("/<trip_id>", methods=["GET"])
def get_trip(user_id, trip_id):

    return domain.get_trip_by_id(trip_id)


@bp.route("/all", methods=["GET"])
def get_trips(user_id):

    return domain.get_all_trips(user_id)


@bp.route("/<trip_id>", methods=["PUT"])
@schema("/update_trip.json")
@token_auth.login_required
def update_trip(user_id, trip_id):

    return domain.update_trip(request.json, user_id, trip_id)


@bp.route("/<trip_id>", methods=["DELETE"])
@token_auth.login_required
def delete_trip(user_id, trip_id):
    domain.delete_trip(user_id, trip_id)

    return {"message": "Trip with `id: %s` has been deleted." % trip_id}
