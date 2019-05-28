from ..helper_functions.get_by_id import get_item_by_id as backend_get_item_by_id
from . import backend


def create_item(item_data):
    item = backend.create_item(item_data)
    item_dict = item.to_dict()

    return item_dict


def get_item_by_id(item_id):
    item = backend_get_item_by_id(item_id)
    item_dict = item.to_dict()

    return item_dict


def get_all_items():
    items = backend.get_all_items()
    items_list = []
    for item in items:
        item_dict = item.to_dict()
        items_list.append(item_dict)

    return items_list


def update_item(item_data, item_id):
    item = backend.update_item(item_data, item_id)
    item_dict = item.to_dict()

    return item_dict


def delete_item(item_id):
    backend.delete_item(item_id)
