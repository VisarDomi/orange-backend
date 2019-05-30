from flask import g
from ..common.exceptions import (
    CannotChangeOthersData,
    CannotDeleteOthersData,
    CannotGetOthersData,
    CannotCreateData,
)
from ..common.models import Admin, Invoice
from ..helper_functions.create import create_entity
from ..helper_functions.get_by_id import get_admin_by_id
from ..helper_functions.common_function import can_it_update


def create_admin(admin_data):
    if g.current_user.admin:
        admin = create_entity(admin_data, Admin)
    else:
        msg = "You can't create data."
        raise CannotCreateData(message=msg)

    return admin


def get_admin(admin_id):
    admin = get_admin_by_id(admin_id)

    return admin


def get_all_admins():
    admins = Admin.query.all()

    return admins


def update_admin(admin_data, admin_id):
    can_update = can_it_update(admin_id=admin_id)
    if can_update:
        admin = get_admin_by_id(admin_id)
        admin.update(**admin_data)
        admin.save()
    else:
        msg = "You can't change other people's data."
        raise CannotChangeOthersData(message=msg)

    return admin


def delete_admin(admin_id):
    can_update = can_it_update(admin_id=admin_id)
    if can_update:
        admin = get_admin_by_id(admin_id)
        admin.delete()
    else:
        msg = "You can't delete other people's data."
        raise CannotDeleteOthersData(message=msg)


def get_all_invoices():
    if g.current_user.admin:
        invoices = Invoice.query.all()
    else:
        msg = "You can't get invoices."
        raise CannotGetOthersData(message=msg)

    return invoices
