import random
from ..common.exceptions import (
    CannotChangeOthersData,
    CannotDeleteOthersData,
    CannotGetOthersData,
    CannotCreateData,
)
from ..models.users import Company
from ..models.items import Itinerary, ItineraryMaster
from ..helper_functions.create import create_entity
from ..helper_functions.get_by_id import get_company_by_id, get_invoice_by_id
from ..helper_functions.common_functions import can_it_update
from ..helper_functions.constants import LETTERS


def create_company(company_data):
    can_update = can_it_update()
    if can_update:
        company = create_entity(company_data, Company)
        letters = LETTERS
        companys = Company.query.all()
        existing_codes = []
        for company in companys:
            existing_codes.append(company.code)
        is_duplicate_code = True
        while is_duplicate_code:
            letter1 = random.choice(letters)
            letter2 = random.choice(letters)
            letter3 = random.choice(letters)
            code = letter1 + letter2 + letter3
            if code not in existing_codes:
                is_duplicate_code = False
        company.code = code
        itinerarys_master = ItineraryMaster.query.all()
        for itinerary_master in itinerarys_master:
            itinerary_data = itinerary_master.to_dict()
            del itinerary_data["id"]
            del itinerary_data["timestamp"]
            itinerary = Itinerary(**itinerary_data)
            company.itinerarys.append(itinerary)
        company.save()
    else:
        msg = "You can't create data."
        raise CannotCreateData(message=msg)

    return company


def get_companys():
    companys = Company.query.all()

    return companys


def get_company(company_id):
    company = get_company_by_id(company_id)

    return company


def update_company(company_data, company_id):
    can_update = can_it_update(company_id=company_id)
    if can_update:
        company = get_company_by_id(company_id)
        company.update(**company_data)
        company.save()
    else:
        msg = "You can't change other people's data."
        raise CannotChangeOthersData(message=msg)

    return company


def delete_company(company_id):
    can_update = can_it_update(company_id=company_id)
    if can_update:
        company = get_company_by_id(company_id)
        company.delete()
    else:
        msg = "You can't delete other people's data."
        raise CannotDeleteOthersData(message=msg)


def get_invoices(company_id):
    can_update = can_it_update(company_id=company_id)
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
    can_update = can_it_update(company_id=company_id)
    if can_update:
        invoice = get_invoice_by_id(invoice_id)
    else:
        msg = "You can't get invoice."
        raise CannotGetOthersData(message=msg)

    return invoice
