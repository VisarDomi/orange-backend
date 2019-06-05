from flask import request
from ..common.validation import schema
from ..bp_auth.views import token_auth
from . import bp
from . import domain


@bp.route("", methods=["POST"])
@schema("create_itinerary_master.json")
@token_auth.login_required
def create_itinerary_master():
    return domain.create_itinerary_master(request.json)


@bp.route("/all", methods=["GET"])
@token_auth.login_required
def get_itinerary_masters():

    return domain.get_itinerary_masters()


@bp.route("/<itinerary_master_id>", methods=["GET"])
@token_auth.login_required
def get_itinerary_master(itinerary_master_id):

    return domain.get_itinerary_master(itinerary_master_id)


# order is route, schema, auth
@bp.route("/<itinerary_master_id>", methods=["PUT"])
@schema("/update_itinerary_master.json")
@token_auth.login_required
def update_itinerary_master(itinerary_master_id):

    return domain.update_itinerary_master(request.json, itinerary_master_id)


@bp.route("/<itinerary_master_id>", methods=["DELETE"])
@token_auth.login_required
def delete_itinerary_master(itinerary_master_id):
    domain.delete_itinerary_master(itinerary_master_id)

    return {"message": "ItineraryMaster with `id: %s` has been deleted." % itinerary_master_id}
