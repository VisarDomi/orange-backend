from ..common.exceptions import (
    CannotChangeOthersData,
    CannotDeleteOthersData,
    CannotCreateData,
    CannotGetOthersData,
)
from ..models.items import Stop
from ..helper_functions.get_by_id import get_stop_by_id
from ..helper_functions.common_functions import can_it_update


def create_stop(stop_data):
    can_update = can_it_update()
    if can_update:
        stop = Stop(**stop_data)
        stop.save()
    else:
        msg = "You can't create data."
        raise CannotCreateData(message=msg)

    return stop


def get_stops():
    can_update = can_it_update()
    if can_update:
        stops = Stop.query.all()
    else:
        msg = "You can't get stops."
        raise CannotGetOthersData(message=msg)

    return stops


def get_stop(stop_id):
    can_update = can_it_update()
    if can_update:
        stop = get_stop_by_id(stop_id)
    else:
        msg = "You can't get stop."
        raise CannotGetOthersData(message=msg)

    return stop


def update_stop(stop_data, stop_id):
    can_update = can_it_update()
    if can_update:
        stop = get_stop_by_id(stop_id)
        stop.update(**stop_data)
        stop.save()
    else:
        msg = "You can't change other people's data."
        raise CannotChangeOthersData(message=msg)

    return stop


def delete_stop(stop_id):
    can_update = can_it_update()
    if can_update:
        stop = get_stop_by_id(stop_id)
        stop.delete()
    else:
        msg = "You can't delete other people's data."
        raise CannotDeleteOthersData(message=msg)
