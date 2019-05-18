from flask import request
from . import bp
from . import domain
from ..common.validation import schema
from ..bp_auth.views import token_auth


@bp.route("", methods=["POST"])
@schema("create_car.json")
@token_auth.login_required
def create_car(user_id):

    return domain.create_car(request.json, user_id)


@bp.route("/<car_id>", methods=["GET"])
def get_car(user_id, car_id):

    return domain.get_car_by_id(car_id)


@bp.route("/all", methods=["GET"])
def get_cars(user_id):

    return domain.get_all_cars(user_id)


@bp.route("/<car_id>", methods=["PUT"])
@schema("/update_car.json")
@token_auth.login_required
def update_car(user_id, car_id):

    return domain.update_car(request.json, user_id, car_id)


@bp.route("/<car_id>", methods=["DELETE"])
@token_auth.login_required
def delete_car(user_id, car_id):
    domain.delete_car(user_id, car_id)

    return {"message": "Trip with `id: %s` has been deleted." % car_id}
