from flask import g
from ..common.exceptions import (
    CannotChangeOthersData,
    CannotDeleteOthersData,
)
from ..common.models import Driver
from ..helper_functions.get_by_id import get_driver_by_id


def create_driver(driver_data):
    driver = Driver(**driver_data)
    driver.save()

    return driver


def get_all_drivers():
    drivers = Driver.query.all()

    return drivers


def update_driver(driver_data, driver_id):
    if int(driver_id) == g.current_user.id:
        driver = get_driver_by_id(driver_id)
        driver.update(**driver_data)
        driver.save()
    else:
        msg = "You can't change other people's data."
        raise CannotChangeOthersData(message=msg)

    return driver


def delete_driver(driver_id):
    if int(driver_id) == g.current_user.id:
        driver = get_driver_by_id(driver_id)
        driver.delete()
    else:
        msg = "You can't delete other people's data."
        raise CannotDeleteOthersData(message=msg)