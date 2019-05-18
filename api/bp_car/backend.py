from flask import g
from ..common.exceptions import (
    CannotChangeOthersData,
    CannotDeleteOthersData,
)
from ..common.models import Car
from ..helper_functions.get_by_id import get_car_by_id


def create_car(car_data, user_id):
    if int(user_id) == g.current_user.id:
        car = Car(**car_data)
        car.owner = g.current_user
        car.save()
    else:
        msg = f"You can't change other people's data."
        raise CannotChangeOthersData(message=msg)

    return car


def get_all_cars(user_id):
    cars = Car.query.filter(Car.owner_id == user_id).all()

    return cars


def update_car(car_data, user_id, car_id):
    if int(user_id) == g.current_user.id:
        car = get_car_by_id(car_id)
        car.update(**car_data)
        car.save()
    else:
        msg = f"You can't change other people's data."
        raise CannotChangeOthersData(message=msg)

    return car


def delete_car(user_id, car_id):
    if int(user_id) == g.current_user.id:
        car = get_car_by_id(car_id)
        car.delete()
    else:
        msg = "You can't delete other people's data."
        raise CannotDeleteOthersData(message=msg)
