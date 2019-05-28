from flask import request
from ..common.validation import schema
from ..bp_auth.views import token_auth
from . import bp
from . import domain


@bp.route("", methods=["POST"])
@schema("create_invoice.json")
def create_invoice():
    return domain.create_invoice(request.json)


@bp.route("/<invoice_id>", methods=["GET"])
def get_invoice(invoice_id):

    return domain.get_invoice_by_id(invoice_id)


@bp.route("/all", methods=["GET"])
def get_invoices():

    return domain.get_all_invoices()


# order is route, schema, auth
@bp.route("/<invoice_id>", methods=["PUT"])
@schema("/update_invoice.json")
@token_auth.login_required
def update_invoice(invoice_id):

    return domain.update_invoice(request.json, invoice_id)


@bp.route("/<invoice_id>", methods=["DELETE"])
@token_auth.login_required
def delete_invoice(invoice_id):
    domain.delete_invoice(invoice_id)

    return {"message": "Invoice with `id: %s` has been deleted." % invoice_id}
