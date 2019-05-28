from flask import g
from ..common.exceptions import (
    CannotChangeOthersData,
    CannotDeleteOthersData,
)
from ..common.models import Item
from ..helper_functions.get_by_id import get_item_by_id


def create_item(item_data):
    item = Item(**item_data)
    item.save()

    return item


def get_all_items():
    items = Item.query.all()

    return items


def update_item(item_data, item_id):
    if int(item_id) == g.current_user.id:
        item = get_item_by_id(item_id)
        item.update(**item_data)
        item.save()
    else:
        msg = "You can't change other people's data."
        raise CannotChangeOthersData(message=msg)

    return item


def delete_item(item_id):
    if int(item_id) == g.current_user.id:
        item = get_item_by_id(item_id)
        item.delete()
    else:
        msg = "You can't delete other people's data."
        raise CannotDeleteOthersData(message=msg)
