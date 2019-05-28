from ..helper_functions.get_by_id import get_reservation_by_id as backend_get_reservation_by_id
from . import backend


def create_reservation(reservation_data):
    reservation = backend.create_reservation(reservation_data)
    reservation_dict = reservation.to_dict()

    return reservation_dict


def get_reservation_by_id(reservation_id):
    reservation = backend_get_reservation_by_id(reservation_id)
    reservation_dict = reservation.to_dict()

    return reservation_dict


def get_all_reservations():
    reservations = backend.get_all_reservations()
    reservations_list = []
    for reservation in reservations:
        reservation_dict = reservation.to_dict()
        reservations_list.append(reservation_dict)

    return reservations_list


def update_reservation(reservation_data, reservation_id):
    reservation = backend.update_reservation(reservation_data, reservation_id)
    reservation_dict = reservation.to_dict()

    return reservation_dict


def delete_reservation(reservation_id):
    backend.delete_reservation(reservation_id)
