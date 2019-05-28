from flask import g
from ..common.exceptions import (
    CannotChangeOthersData,
    CannotDeleteOthersData,
)
from ..common.models import Invoice
from ..helper_functions.get_by_id import get_invoice_by_id


def create_invoice(invoice_data):
    invoice = Invoice(**invoice_data)
    invoice.save()

    return invoice


def get_all_invoices():
    invoices = Invoice.query.all()

    return invoices


def update_invoice(invoice_data, invoice_id):
    if int(invoice_id) == g.current_user.id:
        invoice = get_invoice_by_id(invoice_id)
        invoice.update(**invoice_data)
        invoice.save()
    else:
        msg = "You can't change other people's data."
        raise CannotChangeOthersData(message=msg)

    return invoice


def delete_invoice(invoice_id):
    if int(invoice_id) == g.current_user.id:
        invoice = get_invoice_by_id(invoice_id)
        invoice.delete()
    else:
        msg = "You can't delete other people's data."
        raise CannotDeleteOthersData(message=msg)
