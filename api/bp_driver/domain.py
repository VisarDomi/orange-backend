from . import backend


def create_driver(driver_data):
    driver = backend.create_driver(driver_data)
    driver_dict = driver.to_dict()

    return driver_dict


def get_drivers():
    drivers = backend.get_drivers()
    drivers_list = []
    for driver in drivers:
        driver_dict = driver.to_dict()
        drivers_list.append(driver_dict)

    return drivers_list


def get_driver_by_id(driver_id):
    driver = backend.get_driver(driver_id)
    driver_dict = driver.to_dict()

    return driver_dict


def update_driver(driver_data, driver_id):
    driver = backend.update_driver(driver_data, driver_id)
    driver_dict = driver.to_dict()

    return driver_dict


def delete_driver(driver_id):
    backend.delete_driver(driver_id)
