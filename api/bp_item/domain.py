from . import backend


def create_item(item_data, company_id, reservation_id, invoice_id):
    item = backend.create_item(item_data, company_id, reservation_id, invoice_id)
    item_dict = item.to_dict()

    return item_dict


def get_item_by_id(item_id, company_id, reservation_id, invoice_id):
    item = backend.get_item(item_id, company_id, reservation_id, invoice_id)
    item_dict = item.to_dict()

    return item_dict


def get_all_items(company_id, reservation_id, invoice_id):
    items = backend.get_all_items(company_id, reservation_id, invoice_id)
    items_list = []
    for item in items:
        item_dict = item.to_dict()
        items_list.append(item_dict)

    return items_list


def update_item(item_data, item_id, company_id, reservation_id, invoice_id):
    item = backend.update_item(item_data, item_id, company_id, reservation_id, invoice_id)
    item_dict = item.to_dict()

    return item_dict


def delete_item(item_id, company_id, reservation_id, invoice_id):
    backend.delete_item(item_id, company_id, reservation_id, invoice_id)
