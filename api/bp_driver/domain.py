from . import backend
from ..helper_functions.items_to_dict import reservation_to_dict
from ..helper_functions.users_to_dict import driver_to_dict
from ..helper_functions.constants import EXCLUDE_CREATE, EXCLUDE_GET


def create_driver(driver_data):
    driver = backend.create_driver(driver_data)
    driver_dict = driver_to_dict(driver, EXCLUDE_CREATE)

    return driver_dict


def get_drivers():
    drivers = backend.get_drivers()
    drivers_list = []
    for driver in drivers:
        driver_dict = driver_to_dict(driver, EXCLUDE_GET)
        drivers_list.append(driver_dict)

    return drivers_list


def get_driver(driver_id):
    driver = backend.get_driver(driver_id)
    driver_dict = driver_to_dict(driver, EXCLUDE_GET)

    return driver_dict


def update_driver(driver_data, driver_id):
    driver = backend.update_driver(driver_data, driver_id)
    driver_dict = driver_to_dict(driver, EXCLUDE_GET)

    return driver_dict


def delete_driver(driver_id):
    backend.delete_driver(driver_id)


def get_reservations(driver_id):
    reservations = backend.get_reservations(driver_id)
    reservations_list = []
    for reservation in reservations:
        reservation_dict = reservation_to_dict(reservation)
        reservations_list.append(reservation_dict)

    return reservations_list


def get_reservation(driver_id, reservation_id):
    reservation = backend.get_reservation(driver_id, reservation_id)
    reservation_dict = reservation_to_dict(reservation)

    return reservation_dict


def update_reservation(reservation_data, driver_id, reservation_id):
    reservation = backend.update_reservation(
        reservation_data, driver_id, reservation_id
    )
    reservation_dict = reservation_to_dict(reservation)

    return reservation_dict
