from ..common.exceptions import (
    CannotChangeOthersData,
    CannotDeleteOthersData,
    CannotCreateData,
    CannotGetOthersData,
)
from ..models.items import Itinerary
from ..helper_functions.get_by_id import get_itinerary_by_id, get_company_by_id
from ..helper_functions.common_functions import can_it_update


def create_itinerary(itinerary_data, company_id):
    can_update = can_it_update(company_id=company_id)
    if can_update:
        company = get_company_by_id(company_id)
        itinerary = Itinerary(**itinerary_data)
        itinerary.company = company
        itinerary.save()
        itinerary.save()
    else:
        msg = "You can't create data."
        raise CannotCreateData(message=msg)

    return itinerary


def get_itinerarys(company_id):
    can_update = can_it_update(company_id=company_id)
    if can_update:
        company = get_company_by_id(company_id)
        itinerarys = company.itinerarys.all()
    else:
        msg = "You can't get itinerarys."
        raise CannotGetOthersData(message=msg)

    return itinerarys


def get_itinerary(itinerary_id, company_id):
    can_update = can_it_update(company_id=company_id)
    if can_update:
        itinerary = get_itinerary_by_id(itinerary_id)
    else:
        msg = "You can't get itinerary."
        raise CannotGetOthersData(message=msg)

    return itinerary


def update_itinerary(itinerary_data, itinerary_id, company_id):
    can_update = can_it_update(company_id=company_id)
    if can_update:
        itinerary = get_itinerary_by_id(itinerary_id)
        itinerary.update(**itinerary_data)
        itinerary.save()
    else:
        msg = "You can't change other people's data."
        raise CannotChangeOthersData(message=msg)

    return itinerary


def delete_itinerary(itinerary_id, company_id):
    can_update = can_it_update(company_id=company_id)
    if can_update:
        itinerary = get_itinerary_by_id(itinerary_id)
        itinerary.delete()
    else:
        msg = "You can't delete other people's data."
        raise CannotDeleteOthersData(message=msg)
