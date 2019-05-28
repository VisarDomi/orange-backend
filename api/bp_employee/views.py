from flask import request
from ..common.validation import schema
from ..bp_auth.views import token_auth
from . import bp
from . import domain


@bp.route("", methods=["POST"])
@schema("create_employee.json")
def create_employee():
    return domain.create_employee(request.json)


@bp.route("/<employee_id>", methods=["GET"])
def get_employee(employee_id):

    return domain.get_employee_by_id(employee_id)


@bp.route("/all", methods=["GET"])
def get_employees():

    return domain.get_all_employees()


# order is route, schema, auth
@bp.route("/<employee_id>", methods=["PUT"])
@schema("/update_employee.json")
@token_auth.login_required
def update_employee(employee_id):

    return domain.update_employee(request.json, employee_id)


@bp.route("/<employee_id>", methods=["DELETE"])
@token_auth.login_required
def delete_employee(employee_id):
    domain.delete_employee(employee_id)

    return {"message": "Employee with `id: %s` has been deleted." % employee_id}