from . import backend
from ..helper_functions.get_by_id import get_car_by_id as backend_get_car_by_id


def create_car(car_data, user_id):
    car = backend.create_car(car_data, user_id)
    car_dict = car.to_dict()

    return car_dict


def get_car_by_id(car_id):
    car = backend_get_car_by_id(car_id)
    car_dict = car.to_dict()

    return car_dict


def get_all_cars(user_id):
    cars = backend.get_all_cars(user_id)
    cars_list = []
    for car in cars:
        car_dict = car.to_dict()
        cars_list += [car_dict]

    return cars_list


def update_car(car_data, user_id, car_id):
    car = backend.update_car(car_data, user_id, car_id)
    car_dict = car.to_dict()

    return car_dict


def delete_car(user_id, car_id):
    backend.delete_car(user_id, car_id)
