from . import backend


def create_invoice(invoice_data, reservation_id):
    invoice = backend.create_invoice(invoice_data, reservation_id)
    invoice_dict = invoice.to_dict()

    return invoice_dict


def get_invoices(reservation_id):
    invoices = backend.get_invoices(reservation_id)
    invoices_list = []
    for invoice in invoices:
        invoice_dict = invoice.to_dict()
        invoices_list.append(invoice_dict)

    return invoices_list


def get_invoice_by_id(invoice_id, reservation_id):
    invoice = backend.get_invoice(invoice_id, reservation_id)
    invoice_dict = invoice.to_dict()

    return invoice_dict


def update_invoice(invoice_data, invoice_id, reservation_id):
    invoice = backend.update_invoice(invoice_data, invoice_id, reservation_id)
    invoice_dict = invoice.to_dict()

    return invoice_dict


def delete_invoice(invoice_id, reservation_id):
    backend.delete_invoice(invoice_id, reservation_id)
