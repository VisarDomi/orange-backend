from ..common.exceptions import (
    CannotChangeOthersData,
    CannotDeleteOthersData,
    CannotCreateData,
    CannotGetOthersData,
)
from ..models.items import Invoice, Item
from ..helper_functions.get_entity_by_id import (
    get_invoice_by_id,
    get_reservation_by_id,
    get_item_by_id,
)
from ..helper_functions.common_functions import can_it_update


def create_invoice(invoice_data, reservation_id):
    can_update = can_it_update()
    if can_update:
        ref = invoice_data.pop("ref")
        items_data = invoice_data.pop("items")
        invoice = Invoice(**invoice_data)
        invoice.save()
        reservation = get_reservation_by_id(reservation_id)
        invoice.reservation = reservation
        code = reservation.company.code
        reservation.company.invoice_number = int(ref)
        reservation.save()
        invoice.ref = code + ref
        for item_data in items_data:
            item = Item(**item_data)
            item.invoice = invoice
            item.save()
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
        items_data = []
        try:
            items_data = invoice_data.pop("items")
        except KeyError:
            pass
        ref = invoice_data.pop("ref")
        invoice = get_invoice_by_id(invoice_id)
        invoice.update(**invoice_data)
        reservation = get_reservation_by_id(reservation_id)
        invoice.reservation = reservation
        code = reservation.company.code
        reservation.company.invoice_number = int(ref)
        reservation.save()
        invoice.ref = code + ref
        if items_data:
            for item_data in items_data:
                item_id = item_data["id"]
                item = get_item_by_id(item_id)
                item.invoice = invoice
                item.update(**item_data)
                item.save()
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
