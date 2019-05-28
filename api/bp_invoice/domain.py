from ..helper_functions.get_by_id import get_invoice_by_id as backend_get_invoice_by_id
from . import backend


def create_invoice(invoice_data):
    invoice = backend.create_invoice(invoice_data)
    invoice_dict = invoice.to_dict()

    return invoice_dict


def get_invoice_by_id(invoice_id):
    invoice = backend_get_invoice_by_id(invoice_id)
    invoice_dict = invoice.to_dict()

    return invoice_dict


def get_all_invoices():
    invoices = backend.get_all_invoices()
    invoices_list = []
    for invoice in invoices:
        invoice_dict = invoice.to_dict()
        invoices_list.append(invoice_dict)

    return invoices_list


def update_invoice(invoice_data, invoice_id):
    invoice = backend.update_invoice(invoice_data, invoice_id)
    invoice_dict = invoice.to_dict()

    return invoice_dict


def delete_invoice(invoice_id):
    backend.delete_invoice(invoice_id)
