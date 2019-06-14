from ..common.exceptions import (
    CannotChangeOthersData,
    CannotDeleteOthersData,
    CannotGetOthersData,
    CannotCreateData,
)
from ..models.users import Secretary
from ..helper_functions.get_entity_by_id import (
    get_reservation_by_id,
    get_secretary_by_id,
    get_company_by_id,
)
from ..helper_functions.common_functions import (
    can_it_update,
    is_it_head_secretary,
)
from ..helper_functions.crud_entity import create_entity


def create_secretary(secretary_data, company_id):
    is_head_secretary = is_it_head_secretary(company_id)
    can_update = can_it_update()
    if can_update or is_head_secretary:
        secretary = create_entity(secretary_data, Secretary)
        company = get_company_by_id(company_id)
        secretary.company = company
        secretary.save()
    else:
        msg = "You can't create data."
        raise CannotCreateData(message=msg)

    return secretary


def get_secretarys(company_id):
    is_head_secretary = is_it_head_secretary(company_id)
    can_update = can_it_update()
    if can_update or is_head_secretary:
        company = get_company_by_id(company_id)
        secretarys = company.secretarys.all()
    else:
        msg = "You can't get secretarys."
        raise CannotGetOthersData(message=msg)

    return secretarys


def get_secretary(secretary_id, company_id):
    is_head_secretary = is_it_head_secretary(company_id)
    can_update = can_it_update(secretary_id=secretary_id)
    if can_update or is_head_secretary:
        secretary = get_secretary_by_id(secretary_id)
    else:
        msg = "You can't get secretary."
        raise CannotGetOthersData(message=msg)

    return secretary


def update_secretary(secretary_data, secretary_id, company_id):
    is_head_secretary = is_it_head_secretary(company_id)
    can_update = can_it_update(secretary_id=secretary_id)
    if can_update or is_head_secretary:
        secretary = get_secretary_by_id(secretary_id)
        secretary.update(**secretary_data)
        secretary.save()
    else:
        msg = "You can't change other people's data."
        raise CannotChangeOthersData(message=msg)

    return secretary


def delete_secretary(secretary_id, company_id):
    is_head_secretary = is_it_head_secretary(company_id)
    can_update = can_it_update(secretary_id=secretary_id)
    if can_update or is_head_secretary:
        secretary = get_secretary_by_id(secretary_id)
        secretary.delete()
    else:
        msg = "You can't delete other people's data."
        raise CannotDeleteOthersData(message=msg)


def get_reservations(secretary_id, company_id):
    is_head_secretary = is_it_head_secretary(company_id)
    can_update = can_it_update(secretary_id=secretary_id)
    if can_update or is_head_secretary:
        secretary = get_secretary_by_id(secretary_id)
        reservations = []
        for reservation in secretary.reservations.all():
            reservations.append(reservation)
    else:
        msg = "You can't get reservations."
        raise CannotGetOthersData(message=msg)

    return reservations


def get_reservation(secretary_id, company_id, reservation_id):
    is_head_secretary = is_it_head_secretary(company_id)
    can_update = can_it_update(secretary_id=secretary_id)
    if can_update or is_head_secretary:
        reservation = get_reservation_by_id(reservation_id)
    else:
        msg = "You can't get reservations."
        raise CannotGetOthersData(message=msg)

    return reservation
