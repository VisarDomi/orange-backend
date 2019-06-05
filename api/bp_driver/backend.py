from ..common.exceptions import CannotGetOthersData
from ..helper_functions.get_by_id import get_reservation_by_id, get_driver_by_id
from ..helper_functions.common_functions import can_it_update


def get_reservations(driver_id):
    can_update = can_it_update(driver_id=driver_id)
    if can_update:
        driver = get_driver_by_id(driver_id)
        reservations = driver.reservations
    else:
        msg = "You can't get reservations."
        raise CannotGetOthersData(message=msg)

    return reservations


def get_reservation(driver_id, reservation_id):
    can_update = can_it_update(driver_id=driver_id)
    if can_update:
        reservation = get_reservation_by_id(reservation_id)
    else:
        msg = "You can't get reservation."
        raise CannotGetOthersData(message=msg)

    return reservation


def update_reservation(reservation_data, driver_id, reservation_id):
    can_update = can_it_update(driver_id=driver_id)
    if can_update:
        reservation = get_reservation_by_id(reservation_id)
        reservation.update(**reservation_data)
        if reservation_data["status"] == "rejected":
            reservation.driver = None
        reservation.save()
    else:
        msg = "You can't get reservation."
        raise CannotGetOthersData(message=msg)

    return reservation
