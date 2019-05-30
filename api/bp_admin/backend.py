from flask import g
from ..common.exceptions import (
    CannotChangeOthersData,
    CannotDeleteOthersData,
    CannotGetOthersData,
    CannotCreateData,
)
from ..common.models import Admin, Invoice, Reservation
from ..helper_functions.create import create_entity
from ..helper_functions.get_by_id import (
    get_admin_by_id,
    get_invoice_by_id,
    get_reservation_by_id,
)
from ..helper_functions.common_function import can_it_update


def create_admin(admin_data):
    if g.current_user.admin:
        admin = create_entity(admin_data, Admin)
    else:
        msg = "You can't create data."
        raise CannotCreateData(message=msg)

    return admin


def get_admins():
    admins = Admin.query.all()

    return admins


def get_admin(admin_id):
    admin = get_admin_by_id(admin_id)

    return admin


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


def get_invoices():
    if g.current_user.admin:
        invoices = Invoice.query.all()
    else:
        msg = "You can't get invoices."
        raise CannotGetOthersData(message=msg)

    return invoices


def get_invoice(invoice_id):
    if g.current_user.admin:
        invoice = get_invoice_by_id(invoice_id)
    else:
        msg = "You can't get invoice."
        raise CannotGetOthersData(message=msg)

    return invoice


def get_reservations():
    if g.current_user.admin:
        reservations = Reservation.query.all()
    else:
        msg = "You can't get reservations."
        raise CannotGetOthersData(message=msg)

    return reservations


def get_reservation(reservation_id):
    if g.current_user.admin:
        reservation = get_reservation_by_id(reservation_id)
    else:
        msg = "You can't get reservation."
        raise CannotGetOthersData(message=msg)

    return reservation
