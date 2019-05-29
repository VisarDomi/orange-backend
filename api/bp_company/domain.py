from . import backend


def create_company(company_data):
    company = backend.create_company(company_data)
    company_dict = company.to_dict()

    return company_dict


def get_company_by_id(company_id):
    company = backend.get_company(company_id)
    company_dict = company.to_dict()

    return company_dict


def get_all_companys():
    companys = backend.get_all_companys()
    companys_list = []
    for company in companys:
        company_dict = company.to_dict()
        companys_list.append(company_dict)

    return companys_list


def update_company(company_data, company_id):
    company = backend.update_company(company_data, company_id)
    company_dict = company.to_dict()

    return company_dict


def delete_company(company_id):
    backend.delete_company(company_id)


def get_all_invoices(company_id):
    invoices = backend.get_all_invoices(company_id)
    invoices_list = []
    for invoice in invoices:
        invoice_dict = invoice.to_dict()
        invoices_list.append(invoice_dict)

    return invoices_list
