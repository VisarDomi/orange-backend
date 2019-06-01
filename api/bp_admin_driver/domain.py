from . import backend


def create_driver(driver_data):
    driver = backend.create_driver(driver_data)
    driver_dict = driver.to_dict()

    return driver_dict


def get_drivers():
    drivers = backend.get_drivers()
    drivers_list = []
    for driver in drivers:
        reservation_list = []
        for reservation in driver.reservations.all():
            reservation_list.append(reservation.to_dict())
        driver_dict = driver.to_dict()
        driver_dict["reservations"] = reservation_list
        drivers_list.append(driver_dict)

    return drivers_list


def get_driver(driver_id):
    driver = backend.get_driver(driver_id)
    reservation_list = []
    for reservation in driver.reservations.all():
        reservation_list.append(reservation.to_dict())
    driver_dict = driver.to_dict()
    driver_dict["reservations"] = reservation_list

    return driver_dict


def update_driver(driver_data, driver_id):
    driver = backend.update_driver(driver_data, driver_id)
    reservation_list = []
    for reservation in driver.reservations.all():
        reservation_list.append(reservation.to_dict())
    driver_dict = driver.to_dict()
    driver_dict["reservations"] = reservation_list

    return driver_dict


def delete_driver(driver_id):
    backend.delete_driver(driver_id)
