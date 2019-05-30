from flask import g
from ..common.exceptions import (
    CannotChangeOthersData,
    CannotDeleteOthersData,
    CannotCreateData,
    CannotGetOthersData,
)
from ..common.models import Item
from ..helper_functions.get_by_id import (
    get_item_by_id,
    get_invoice_by_id,
)


def create_item(item_data, reservation_id, invoice_id):
    if g.current_user.admin:
        item = Item(**item_data)
        invoice = get_invoice_by_id(invoice_id)
        item.invoice = invoice
        item.save()
    else:
        msg = "You can't create data."
        raise CannotCreateData(message=msg)

    return item


def get_item(item_id, reservation_id, invoice_id):
    if g.current_user.admin:
        item = get_item_by_id(item_id)
    else:
        msg = "You can't get item."
        raise CannotGetOthersData(message=msg)

    return item


def get_all_items(reservation_id, invoice_id):
    if g.current_user.admin:
        invoice = get_invoice_by_id(invoice_id)
        items = invoice.items.all()
    else:
        msg = "You can't get items."
        raise CannotGetOthersData(message=msg)

    return items


def update_item(item_data, item_id, reservation_id, invoice_id):
    if g.current_user.admin:
        item = get_item_by_id(item_id)
        item.update(**item_data)
        item.save()
    else:
        msg = "You can't change other's data."
        raise CannotChangeOthersData(message=msg)

    return item


def delete_item(item_id, reservation_id, invoice_id):
    if g.current_user.admin:
        item = get_item_by_id(item_id)
        item.delete()
    else:
        msg = "You can't delete other's data."
        raise CannotDeleteOthersData(message=msg)
