from ..common.exceptions import (
    CannotChangeOthersData,
    CannotDeleteOthersData,
    CannotCreateData,
    CannotGetOthersData,
)
from ..models.items import ItineraryMaster
from ..helper_functions.get_entity_by_id import get_itinerary_master_by_id
from ..helper_functions.common_functions import can_it_update


def create_itinerary_master(itinerary_master_data):
    can_update = can_it_update()
    if can_update:
        itinerary_master = ItineraryMaster(**itinerary_master_data)
        itinerary_master.save()
    else:
        msg = "You can't create data."
        raise CannotCreateData(message=msg)

    return itinerary_master


def get_itinerary_masters():
    can_update = can_it_update()
    if can_update:
        itinerary_masters = ItineraryMaster.query.all()
    else:
        msg = "You can't get itinerary_masters."
        raise CannotGetOthersData(message=msg)

    return itinerary_masters


def get_itinerary_master(itinerary_master_id):
    can_update = can_it_update()
    if can_update:
        itinerary_master = get_itinerary_master_by_id(itinerary_master_id)
    else:
        msg = "You can't get itinerary_master."
        raise CannotGetOthersData(message=msg)

    return itinerary_master


def update_itinerary_master(itinerary_master_data, itinerary_master_id):
    can_update = can_it_update()
    if can_update:
        itinerary_master = get_itinerary_master_by_id(itinerary_master_id)
        itinerary_master.update(**itinerary_master_data)
        itinerary_master.save()
    else:
        msg = "You can't change other people's data."
        raise CannotChangeOthersData(message=msg)

    return itinerary_master


def delete_itinerary_master(itinerary_master_id):
    can_update = can_it_update()
    if can_update:
        itinerary_master = get_itinerary_master_by_id(itinerary_master_id)
        itinerary_master.delete()
    else:
        msg = "You can't delete other people's data."
        raise CannotDeleteOthersData(message=msg)
