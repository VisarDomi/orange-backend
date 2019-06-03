from . import backend


def create_company(company_data):
    company = backend.create_company(company_data)
    company_dict = company.to_dict()

    return company_dict


def get_companys():
    companys = backend.get_companys()
    companys_list = []
    for company in companys:
        company_dict = company.to_dict()
        companys_list.append(company_dict)

    return companys_list


def get_company(company_id):
    company = backend.get_company(company_id)
    company_dict = company.to_dict()

    return company_dict


def update_company(company_data, company_id):
    company = backend.update_company(company_data, company_id)
    company_dict = company.to_dict()

    return company_dict


def delete_company(company_id):
    backend.delete_company(company_id)


def get_invoices(company_id):
    invoices = backend.get_invoices(company_id)
    invoices_list = []
    for invoice in invoices:
        invoice_dict = invoice.to_dict()
        employees = []
        for employee in invoice.reservation.employees.all():
            employees.append(employee.to_dict())
        if invoice.reservation.destination:
            invoice_dict["destination"] = invoice.reservation.destination
        else:
            invoice_dict["destination"] = ""
        invoice_dict["employees"] = employees
        invoices_list.append(invoice_dict)

    return invoices_list


def get_invoice(company_id, invoice_id):
    invoice = backend.get_invoice(company_id, invoice_id)
    invoice_dict = invoice.to_dict()
    employees = []
    for employee in invoice.reservation.employees.all():
        employees.append(employee.to_dict())
    if invoice.reservation.destination:
        invoice_dict["destination"] = invoice.reservation.destination
    else:
        invoice_dict["destination"] = ""
    invoice_dict["employees"] = employees

    return invoice_dict
