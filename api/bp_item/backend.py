from ..common.exceptions import CannotChangeOthersData, CannotDeleteOthersData
from ..common.models import Item
from ..helper_functions.get_by_id import (
    get_item_by_id,
    get_reservation_by_id,
    get_invoice_by_id,
)
from ..helper_functions.common_function import can_it_update


def create_item(item_data, company_id, reservation_id, invoice_id):
    can_update = can_it_update(company_id=company_id)
    if can_update:
        item = Item(**item_data)
        invoice = get_invoice_by_id(invoice_id)
        item.invoice = invoice
        item.save()
    else:
        msg = "You can't change other people's data."
        raise CannotChangeOthersData(message=msg)

    return item


def get_item(item_id, company_id, reservation_id, invoice_id):
    item = get_item_by_id(item_id)

    return item


def get_all_items(company_id, reservation_id, invoice_id):
    reservation = get_reservation_by_id(reservation_id)
    invoices = reservation.invoices.all()
    items = []
    for invoice in invoices:
        invoice_items = invoice.items.all()
        items.append(invoice_items)

    return items


def update_item(item_data, item_id, company_id, reservation_id, invoice_id):
    can_update = can_it_update(company_id=company_id)
    if can_update:
        item = get_item_by_id(item_id)
        item.update(**item_data)
        item.save()
    else:
        msg = "You can't change other people's data."
        raise CannotChangeOthersData(message=msg)

    return item


def delete_item(item_id, company_id, reservation_id, invoice_id):
    can_update = can_it_update(company_id=company_id)
    if can_update:
        item = get_item_by_id(item_id)
        item.delete()
    else:
        msg = "You can't delete other people's data."
        raise CannotDeleteOthersData(message=msg)
