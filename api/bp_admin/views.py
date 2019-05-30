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


@bp.route("/all", methods=["GET"])
@token_auth.login_required
def get_admins():

    return domain.get_admins()


@bp.route("/<admin_id>", methods=["GET"])
@token_auth.login_required
def get_admin(admin_id):

    return domain.get_admin(admin_id)


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


@bp.route("/invoice/all", methods=["GET"])
@token_auth.login_required
def get_invoices():

    return domain.get_invoices()


@bp.route("/invoice/<invoice_id>", methods=["GET"])
@token_auth.login_required
def get_invoice(invoice_id):

    return domain.get_invoice(invoice_id)


@bp.route("/reservation/all", methods=["GET"])
@token_auth.login_required
def get_reservations():

    return domain.get_reservations()


@bp.route("/reservation/<reservation_id>", methods=["GET"])
@token_auth.login_required
def get_reservation(reservation_id):

    return domain.get_reservation(reservation_id)


@bp.route("/reservation/<reservation_id>", methods=["PUT"])
@schema("/update_reservation.json")
@token_auth.login_required
def update_reservation(reservation_id):

    return domain.update_reservation(request.json, reservation_id)
