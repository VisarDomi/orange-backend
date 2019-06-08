from . import backend
from ..helper_functions.dict import reservation_to_dict


def create_reservation(reservation_data, company_id):
    reservation = backend.create_reservation(reservation_data, company_id)
    reservation_dict = reservation_to_dict(reservation)

    return reservation_dict


def get_reservations(company_id):
    reservations = backend.get_reservations(company_id)
    reservations_list = []
    for reservation in reservations:
        reservation_dict = reservation_to_dict(reservation)
        reservations_list.append(reservation_dict)

    return reservations_list


def get_reservation(reservation_id, company_id):
    reservation = backend.get_reservation(reservation_id, company_id)
    reservation_dict = reservation_to_dict(reservation)

    return reservation_dict


def update_reservation(reservation_data, reservation_id, company_id):
    reservation = backend.update_reservation(
        reservation_data, reservation_id, company_id
    )
    reservation_dict = reservation_to_dict(reservation)

    return reservation_dict


def delete_reservation(reservation_id, company_id):
    backend.delete_reservation(reservation_id, company_id)
