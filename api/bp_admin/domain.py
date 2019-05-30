from . import backend


def create_admin(admin_data):
    admin = backend.create_admin(admin_data)
    admin_dict = admin.to_dict()

    return admin_dict


def get_admin_by_id(admin_id):
    admin = backend.get_admin(admin_id)
    admin_dict = admin.to_dict()

    return admin_dict


def get_all_admins():
    admins = backend.get_all_admins()
    admins_list = []
    for admin in admins:
        admin_dict = admin.to_dict()
        admins_list.append(admin_dict)

    return admins_list


def update_admin(admin_data, admin_id):
    admin = backend.update_admin(admin_data, admin_id)
    admin_dict = admin.to_dict()

    return admin_dict


def delete_admin(admin_id):
    backend.delete_admin(admin_id)


def get_all_invoices():
    invoices = backend.get_all_invoices()
    invoices_list = []
    for invoice in invoices:
        invoice_dict = invoice.to_dict()
        invoices_list.append(invoice_dict)

    return invoices_list
