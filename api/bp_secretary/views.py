from flask import request
from ..common.validation import schema
from ..bp_auth.views import token_auth
from . import bp
from . import domain


@bp.route("", methods=["POST"])
@schema("create_secretary.json")
@token_auth.login_required
def create_secretary(company_id):

    return domain.create_secretary(request.json, company_id)


@bp.route("/all", methods=["GET"])
@token_auth.login_required
def get_secretarys(company_id):

    return domain.get_secretarys(company_id)


@bp.route("/<secretary_id>", methods=["GET"])
@token_auth.login_required
def get_secretary(secretary_id, company_id):

    return domain.get_secretary(secretary_id, company_id)


# order is route, schema, auth
@bp.route("/<secretary_id>", methods=["PUT"])
@schema("/update_secretary.json")
@token_auth.login_required
def update_secretary(secretary_id, company_id):

    return domain.update_secretary(request.json, secretary_id, company_id)


@bp.route("/<secretary_id>", methods=["DELETE"])
@token_auth.login_required
def delete_secretary(secretary_id, company_id):
    domain.delete_secretary(secretary_id, company_id)

    return {"message": "Secretary with `id: %s` has been deleted." % secretary_id}


@bp.route("/<secretary_id>/reservation/all", methods=["GET"])
@token_auth.login_required
def get_reservations(secretary_id, company_id):

    return domain.get_reservations(secretary_id, company_id)


@bp.route("/<secretary_id>/reservation/<reservation_id>", methods=["GET"])
@token_auth.login_required
def get_reservation(secretary_id, company_id, reservation_id):

    return domain.get_reservation(secretary_id, company_id, reservation_id)
