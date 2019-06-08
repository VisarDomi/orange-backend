from flask import request
from ..common.validation import schema
from ..bp_auth.views import token_auth
from . import bp
from . import domain


@bp.route("", methods=["POST"])
@schema("create_itinerary.json")
@token_auth.login_required
def create_itinerary(company_id):
    return domain.create_itinerary(request.json, company_id)


@bp.route("/all", methods=["GET"])
@token_auth.login_required
def get_itinerarys(company_id):

    return domain.get_itinerarys(company_id)


@bp.route("/<itinerary_id>", methods=["GET"])
@token_auth.login_required
def get_itinerary(itinerary_id, company_id):

    return domain.get_itinerary(itinerary_id, company_id)


# order is route, schema, auth
@bp.route("/<itinerary_id>", methods=["PUT"])
@schema("/update_itinerary.json")
@token_auth.login_required
def update_itinerary(itinerary_id, company_id):

    return domain.update_itinerary(request.json, itinerary_id, company_id)


@bp.route("/<itinerary_id>", methods=["DELETE"])
@token_auth.login_required
def delete_itinerary(itinerary_id, company_id):
    domain.delete_itinerary(itinerary_id, company_id)

    return {"message": "Itinerary with `id: %s` has been deleted." % itinerary_id}
