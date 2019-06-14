from ..common.exceptions import (
    CannotChangeOthersData,
    CannotDeleteOthersData,
    CannotGetOthersData,
    CannotCreateData,
)
from ..models.items import Company
from ..models.users import Secretary
from ..helper_functions.get_entity_by_id import get_company_by_id, get_invoice_by_id
from ..helper_functions.common_functions import can_it_update, get_secretary_id
from ..helper_functions.crud_entity import create_entity
from ..helper_functions.constants import HEAD_SECRETARY


def create_company(company_data):
    can_update = can_it_update()
    if can_update:
        secretary_data = company_data.pop("head_secretary")
        secretary_data["role"] = HEAD_SECRETARY
        company = Company(**company_data)
        secretary = create_entity(secretary_data, Secretary)
        company.save()
        secretary.company = company
        secretary.save()
    else:
        msg = "You can't create data."
        raise CannotCreateData(message=msg)

    return company


def get_companys():
    can_update = can_it_update()
    if can_update:
        companys = Company.query.all()
    else:
        msg = "You can't get companys."
        raise CannotGetOthersData(message=msg)

    return companys


def get_company(company_id):
    secretary_id = get_secretary_id(company_id)
    can_update = can_it_update(secretary_id=secretary_id)
    if can_update:
        company = get_company_by_id(company_id)
    else:
        msg = "You can't get company."
        raise CannotGetOthersData(message=msg)

    return company


def update_company(company_data, company_id):
    can_update = can_it_update()
    if can_update:
        company = get_company_by_id(company_id)
        company.update(**company_data)
        company.save()
    else:
        msg = "You can't change company data."
        raise CannotChangeOthersData(message=msg)

    return company


def delete_company(company_id):
    can_update = can_it_update()
    if can_update:
        company = get_company_by_id(company_id)
        company.delete()
    else:
        msg = "You can't delete other people's data."
        raise CannotDeleteOthersData(message=msg)


def get_invoices(company_id):
    secretary_id = get_secretary_id(company_id)
    can_update = can_it_update(secretary_id=secretary_id)
    if can_update:
        company = get_company_by_id(company_id)
        reservations = company.reservations.all()
        invoices = []
        for reservation in reservations:
            invoices_reservation = reservation.invoices.all()
            for invoice in invoices_reservation:
                invoices.append(invoice)
    else:
        msg = "You can't get invoices."
        raise CannotGetOthersData(message=msg)

    return invoices


def get_invoice(company_id, invoice_id):
    secretary_id = get_secretary_id(company_id)
    can_update = can_it_update(secretary_id=secretary_id)
    if can_update:
        invoice = get_invoice_by_id(invoice_id)
    else:
        msg = "You can't get invoice."
        raise CannotGetOthersData(message=msg)

    return invoice
