from flask import request
from ..common.validation import schema
from ..bp_auth.views import token_auth
from . import bp
from . import domain


@bp.route("/all", methods=["GET"])
@token_auth.login_required
def get_reservations(driver_id):

    return domain.get_reservations(driver_id)


@bp.route("/<reservation_id>", methods=["GET"])
@token_auth.login_required
def get_reservation(driver_id, reservation_id):

    return domain.get_reservation(driver_id, reservation_id)


@bp.route("/<reservation_id>", methods=["PUT"])
@schema("/update_reservation.json")
@token_auth.login_required
def update_reservation(driver_id, reservation_id):

    return domain.update_reservation(request.json, driver_id, reservation_id)
