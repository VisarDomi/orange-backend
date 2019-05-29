from ..common.exceptions import CannotChangeOthersData, CannotDeleteOthersData
from ..common.models import Invoice
from ..helper_functions.get_by_id import get_invoice_by_id, get_reservation_by_id
from ..helper_functions.common_function import can_it_update


def create_invoice(invoice_data, company_id, reservation_id):
    can_update = can_it_update(company_id=company_id)
    if can_update:
        invoice = Invoice(**invoice_data)
        reservation = get_reservation_by_id(reservation_id)
        invoice.reservation = reservation
        invoice.save()
    else:
        msg = "You can't change other people's data."
        raise CannotChangeOthersData(message=msg)

    return invoice


def get_invoice(invoice_id, company_id, reservation_id):
    can_update = can_it_update(company_id=company_id)
    if can_update:
        invoice = get_invoice_by_id(invoice_id)
    else:
        msg = "You can't change other people's data."
        raise CannotChangeOthersData(message=msg)

    return invoice


def get_all_invoices(company_id, reservation_id):
    can_update = can_it_update(company_id=company_id)
    if can_update:
        reservation = get_reservation_by_id(reservation_id)
        invoices = reservation.invoices.all()
    else:
        msg = "You can't change other people's data."
        raise CannotChangeOthersData(message=msg)

    return invoices


def update_invoice(invoice_data, invoice_id, company_id, reservation_id):
    can_update = can_it_update(company_id=company_id)
    if can_update:
        invoice = get_invoice_by_id(invoice_id)
        invoice.update(**invoice_data)
        invoice.save()
    else:
        msg = "You can't change other people's data."
        raise CannotChangeOthersData(message=msg)

    return invoice


def delete_invoice(invoice_id, company_id, reservation_id):
    can_update = can_it_update(company_id=company_id)
    if can_update:
        invoice = get_invoice_by_id(invoice_id)
        invoice.delete()
    else:
        msg = "You can't delete other people's data."
        raise CannotDeleteOthersData(message=msg)
