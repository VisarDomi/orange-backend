from flask import request
from ..common.validation import schema
from ..bp_auth.views import token_auth
from . import bp
from . import domain


@bp.route("", methods=["POST"])
@schema("create_company.json")
@token_auth.login_required
def create_company():

    return domain.create_company(request.json)


@bp.route("/all", methods=["GET"])
@token_auth.login_required
def get_companys():

    return domain.get_companys()


@bp.route("/<company_id>", methods=["GET"])
@token_auth.login_required
def get_company(company_id):

    return domain.get_company(company_id)


# order is route, schema, auth
@bp.route("/<company_id>", methods=["PUT"])
@schema("/update_company.json")
@token_auth.login_required
def update_company(company_id):

    return domain.update_company(request.json, company_id)


@bp.route("/<company_id>", methods=["DELETE"])
@token_auth.login_required
def delete_company(company_id):
    domain.delete_company(company_id)

    return {"message": "Company with `id: %s` has been deleted." % company_id}


@bp.route("/<company_id>/invoice/all", methods=["GET"])
@token_auth.login_required
def get_invoices(company_id):

    return domain.get_invoices(company_id)


@bp.route("/<company_id>/invoice/<invoice_id>", methods=["GET"])
@token_auth.login_required
def get_invoice(company_id, invoice_id):

    return domain.get_invoice(company_id, invoice_id)
