from . import backend
from ..helper_functions.items_to_dict import reservation_to_dict, invoice_to_dict
from ..helper_functions.users_to_dict import admin_to_dict
from ..helper_functions.constants import EXCLUDE_CREATE, EXCLUDE_GET


def create_admin(admin_data):
    admin = backend.create_admin(admin_data)
    admin_dict = admin_to_dict(admin, EXCLUDE_CREATE)

    return admin_dict


def get_admins():
    admins = backend.get_admins()
    admins_list = []
    for admin in admins:
        admin_dict = admin_to_dict(admin, EXCLUDE_GET)
        admins_list.append(admin_dict)

    return admins_list


def get_admin(admin_id):
    admin = backend.get_admin(admin_id)
    admin_dict = admin_to_dict(admin, EXCLUDE_GET)

    return admin_dict


def update_admin(admin_data, admin_id):
    admin = backend.update_admin(admin_data, admin_id)
    admin_dict = admin_to_dict(admin, EXCLUDE_GET)

    return admin_dict


def delete_admin(admin_id):
    backend.delete_admin(admin_id)


def get_invoices():
    invoices = backend.get_invoices()
    invoices_list = []
    for invoice in invoices:
        invoice_dict = invoice_to_dict(invoice)
        invoices_list.append(invoice_dict)

    return invoices_list


def get_invoice(invoice_id):
    invoice = backend.get_invoice(invoice_id)
    invoice_dict = invoice_to_dict(invoice)

    return invoice_dict


def get_reservations():
    reservations = backend.get_reservations()
    reservations_list = []
    for reservation in reservations:
        reservation_dict = reservation_to_dict(reservation)
        reservations_list.append(reservation_dict)

    return reservations_list


def get_reservation(reservation_id):
    reservation = backend.get_reservation(reservation_id)
    reservation_dict = reservation_to_dict(reservation)

    return reservation_dict


def update_reservation(reservation_data, reservation_id):
    reservation = backend.update_reservation(reservation_data, reservation_id)
    reservation_dict = reservation_to_dict(reservation)

    return reservation_dict
