from ..common.exceptions import (
    CannotChangeOthersData,
    CannotDeleteOthersData,
    CannotCreateData,
    CannotGetOthersData,
)
from ..models.items import Invoice
from ..helper_functions.get_by_id import get_invoice_by_id, get_reservation_by_id
from ..helper_functions.common_functions import can_it_update


def create_invoice(invoice_data, reservation_id):
    can_update = can_it_update()
    if can_update:
        ref = False
        try:
            ref = invoice_data.pop("ref")
        except KeyError:
            # msg = "There is no ref in invoice."
            # raise CannotCreateData(message=msg)
            pass
        invoice = Invoice(**invoice_data)
        invoice.save()
        reservation = get_reservation_by_id(reservation_id)
        invoice.reservation = reservation
        code = reservation.company.code
        if ref:
            invoice.ref = code + ref
        else:
            number = str(invoice.id).zfill(5)
            invoice.ref = code + number
        invoice.save()
    else:
        msg = "You can't create data."
        raise CannotCreateData(message=msg)

    return invoice


def get_invoices(reservation_id):
    can_update = can_it_update()
    if can_update:
        reservation = get_reservation_by_id(reservation_id)
        invoices = reservation.invoices.all()
    else:
        msg = "You can't get invoices."
        raise CannotGetOthersData(message=msg)

    return invoices


def update_invoice(invoice_data, invoice_id, reservation_id):
    can_update = can_it_update()
    if can_update:
        invoice = get_invoice_by_id(invoice_id)
        invoice.update(**invoice_data)
        invoice.save()
    else:
        msg = "You can't change other's data."
        raise CannotChangeOthersData(message=msg)

    return invoice


def delete_invoice(invoice_id, reservation_id):
    can_update = can_it_update()
    if can_update:
        invoice = get_invoice_by_id(invoice_id)
        invoice.delete()
    else:
        msg = "You can't delete other's data."
        raise CannotDeleteOthersData(message=msg)
