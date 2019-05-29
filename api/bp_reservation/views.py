from flask import request
from ..common.validation import schema
from ..bp_auth.views import token_auth
from . import bp
from . import domain


@bp.route("", methods=["POST"])
@schema("create_reservation.json")
@token_auth.login_required
def create_reservation(company_id):
    return domain.create_reservation(request.json, company_id)


@bp.route("/<reservation_id>", methods=["GET"])
@token_auth.login_required
def get_reservation(reservation_id, company_id):

    return domain.get_reservation_by_id(reservation_id, company_id)


@bp.route("/all", methods=["GET"])
@token_auth.login_required
def get_reservations(company_id):

    return domain.get_all_reservations(company_id)


# order is route, schema, auth
@bp.route("/<reservation_id>", methods=["PUT"])
@schema("/update_reservation.json")
@token_auth.login_required
def update_reservation(reservation_id, company_id):

    return domain.update_reservation(request.json, reservation_id, company_id)


@bp.route("/<reservation_id>", methods=["DELETE"])
@token_auth.login_required
def delete_reservation(reservation_id, company_id):
    domain.delete_reservation(reservation_id, company_id)

    return {"message": "Reservation with `id: %s` has been deleted." % reservation_id}
