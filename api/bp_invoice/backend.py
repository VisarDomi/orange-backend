from flask import g
from ..common.exceptions import (
    CannotChangeOthersData,
    CannotDeleteOthersData,
    CannotCreateData,
    CannotGetOthersData,
)
from ..models.items import Invoice
from ..helper_functions.get_by_id import get_invoice_by_id, get_reservation_by_id


def create_invoice(invoice_data, reservation_id):
    if g.current_user.admin:
        invoice = Invoice(**invoice_data)
        reservation = get_reservation_by_id(reservation_id)
        invoice.reservation = reservation
        invoice.save()
    else:
        msg = "You can't create data."
        raise CannotCreateData(message=msg)

    return invoice


def get_invoices(reservation_id):
    if g.current_user.admin:
        reservation = get_reservation_by_id(reservation_id)
        invoices = reservation.invoices.all()
    else:
        msg = "You can't get invoices."
        raise CannotGetOthersData(message=msg)

    return invoices


def get_invoice(invoice_id, reservation_id):
    if g.current_user.admin:
        invoice = get_invoice_by_id(invoice_id)
    else:
        msg = "You can't get invoice."
        raise CannotGetOthersData(message=msg)

    return invoice


def update_invoice(invoice_data, invoice_id, reservation_id):
    if g.current_user.admin:
        invoice = get_invoice_by_id(invoice_id)
        invoice.update(**invoice_data)
        invoice.save()
    else:
        msg = "You can't change other's data."
        raise CannotChangeOthersData(message=msg)

    return invoice


def delete_invoice(invoice_id, reservation_id):
    if g.current_user.admin:
        invoice = get_invoice_by_id(invoice_id)
        invoice.delete()
    else:
        msg = "You can't delete other's data."
        raise CannotDeleteOthersData(message=msg)
