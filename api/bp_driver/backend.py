from ..common.exceptions import (
    CannotGetOthersData,
    CannotChangeOthersData,
    CannotDeleteOthersData,
    CannotCreateData,
)
from ..models.users import Driver
from ..helper_functions.create import create_entity
from ..helper_functions.get_by_id import get_reservation_by_id, get_driver_by_id
from ..helper_functions.common_functions import can_it_update


def create_driver(driver_data):
    can_update = can_it_update()
    if can_update:
        driver = create_entity(driver_data, Driver)
    else:
        msg = "You can't create data."
        raise CannotCreateData(message=msg)

    return driver


def get_drivers():
    drivers = Driver.query.all()

    return drivers


def get_driver(driver_id):
    driver = get_driver_by_id(driver_id)

    return driver


def update_driver(driver_data, driver_id):
    can_update = can_it_update(driver_id=driver_id)
    if can_update:
        driver = get_driver_by_id(driver_id)
        driver.update(**driver_data)
        driver.save()
    else:
        msg = "You can't change other people's data."
        raise CannotChangeOthersData(message=msg)

    return driver


def delete_driver(driver_id):
    can_update = can_it_update(driver_id=driver_id)
    if can_update:
        driver = get_driver_by_id(driver_id)
        driver.delete()
    else:
        msg = "You can't delete other people's data."
        raise CannotDeleteOthersData(message=msg)


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
