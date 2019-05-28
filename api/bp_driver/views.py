from flask import request
from ..common.validation import schema
from ..bp_auth.views import token_auth
from . import bp
from . import domain


@bp.route("", methods=["POST"])
@schema("create_driver.json")
def create_driver():
    return domain.create_driver(request.json)


@bp.route("/<driver_id>", methods=["GET"])
def get_driver(driver_id):

    return domain.get_driver_by_id(driver_id)


@bp.route("/all", methods=["GET"])
def get_drivers():

    return domain.get_all_drivers()


# order is route, schema, auth
@bp.route("/<driver_id>", methods=["PUT"])
@schema("/update_driver.json")
@token_auth.login_required
def update_driver(driver_id):

    return domain.update_driver(request.json, driver_id)


@bp.route("/<driver_id>", methods=["DELETE"])
@token_auth.login_required
def delete_driver(driver_id):
    domain.delete_driver(driver_id)

    return {"message": "Driver with `id: %s` has been deleted." % driver_id}
