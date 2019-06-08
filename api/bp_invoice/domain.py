from . import backend
from ..helper_functions.dict import invoice_to_dict


def create_invoice(invoice_data, reservation_id):
    invoice = backend.create_invoice(invoice_data, reservation_id)
    invoice_dict = invoice_to_dict(invoice)

    return invoice_dict


def get_invoices(reservation_id):
    invoices = backend.get_invoices(reservation_id)
    invoices_list = []
    for invoice in invoices:
        invoice_dict = invoice_to_dict(invoice)
        invoices_list.append(invoice_dict)

    return invoices_list


def update_invoice(invoice_data, invoice_id, reservation_id):
    invoice = backend.update_invoice(invoice_data, invoice_id, reservation_id)
    invoice_dict = invoice_to_dict(invoice)

    return invoice_dict


def delete_invoice(invoice_id, reservation_id):
    backend.delete_invoice(invoice_id, reservation_id)
