from flask import request
from ..common.validation import schema
from ..bp_auth.views import token_auth
from . import bp
from . import domain


@bp.route("", methods=["POST"])
@schema("create_item.json")
@token_auth.login_required
def create_item(reservation_id, invoice_id):
    return domain.create_item(request.json, reservation_id, invoice_id)


@bp.route("/<item_id>", methods=["GET"])
@token_auth.login_required
def get_item(item_id, reservation_id, invoice_id):

    return domain.get_item_by_id(item_id, reservation_id, invoice_id)


@bp.route("/all", methods=["GET"])
@token_auth.login_required
def get_items(reservation_id, invoice_id):

    return domain.get_all_items(reservation_id, invoice_id)


# order is route, schema, auth
@bp.route("/<item_id>", methods=["PUT"])
@schema("/update_item.json")
@token_auth.login_required
def update_item(item_id, reservation_id, invoice_id):

    return domain.update_item(request.json, item_id, reservation_id, invoice_id)


@bp.route("/<item_id>", methods=["DELETE"])
@token_auth.login_required
def delete_item(item_id, reservation_id, invoice_id):
    domain.delete_item(item_id, reservation_id, invoice_id)

    return {"message": "Item with `id: %s` has been deleted." % item_id}
