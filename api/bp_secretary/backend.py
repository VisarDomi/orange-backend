from ..common.exceptions import (
    CannotChangeOthersData,
    CannotDeleteOthersData,
    CannotCreateData,
)
from ..models.users import Secretary
from ..helper_functions.create import create_entity
from ..helper_functions.get_by_id import (
    get_reservation_by_id,
    get_secretary_by_id,
    get_company_by_id,
)
from ..helper_functions.common_functions import can_it_update


def create_secretary(secretary_data, company_id):
    can_update = can_it_update(company_id=company_id)
    if can_update:
        secretary = create_entity(secretary_data, Secretary)
        company = get_company_by_id(company_id)
        secretary.company = company
        secretary.save()
    else:
        msg = "You can't create data."
        raise CannotCreateData(message=msg)

    return secretary


def get_secretarys(company_id):
    company = get_company_by_id(company_id)
    secretarys = company.secretarys.all()

    return secretarys


def get_secretary(secretary_id, company_id):
    secretary = get_secretary_by_id(secretary_id)

    return secretary


def update_secretary(secretary_data, secretary_id, company_id):
    can_update = can_it_update(secretary_id=secretary_id)
    if can_update:
        secretary = get_secretary_by_id(secretary_id)
        secretary.update(**secretary_data)
        secretary.save()
    else:
        msg = "You can't change other people's data."
        raise CannotChangeOthersData(message=msg)

    return secretary


def delete_secretary(secretary_id, company_id):
    can_update = can_it_update(secretary_id=secretary_id)
    if can_update:
        secretary = get_secretary_by_id(secretary_id)
        secretary.delete()
    else:
        msg = "You can't delete other people's data."
        raise CannotDeleteOthersData(message=msg)


def get_reservations(secretary_id, company_id):
    secretary = get_secretary_by_id(secretary_id)
    stops = secretary.stops.all()
    reservations = []
    for stop in stops:
        reservation = stop.reservation
        if reservation not in reservations:
            reservations.append(reservation)

    return reservations


def get_reservation(secretary_id, company_id, reservation_id):
    reservation = get_reservation_by_id(reservation_id)

    return reservation
