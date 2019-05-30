from flask import request
from ..common.validation import schema
from ..bp_auth.views import token_auth
from . import bp
from . import domain


@bp.route("", methods=["POST"])
@schema("create_employee.json")
@token_auth.login_required
def create_employee(company_id):

    return domain.create_employee(request.json, company_id)


@bp.route("/all", methods=["GET"])
@token_auth.login_required
def get_employees(company_id):

    return domain.get_employees(company_id)


@bp.route("/<employee_id>", methods=["GET"])
@token_auth.login_required
def get_employee(employee_id, company_id):

    return domain.get_employee(employee_id, company_id)


# order is route, schema, auth
@bp.route("/<employee_id>", methods=["PUT"])
@schema("/update_employee.json")
@token_auth.login_required
def update_employee(employee_id, company_id):

    return domain.update_employee(request.json, employee_id, company_id)


@bp.route("/<employee_id>", methods=["DELETE"])
@token_auth.login_required
def delete_employee(employee_id, company_id):
    domain.delete_employee(employee_id, company_id)

    return {"message": "Employee with `id: %s` has been deleted." % employee_id}
