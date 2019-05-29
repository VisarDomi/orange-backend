from . import backend


def create_reservation(reservation_data, company_id):
    reservation = backend.create_reservation(reservation_data, company_id)
    reservation_dict = reservation.to_dict()

    return reservation_dict


def get_reservation_by_id(reservation_id, company_id):
    reservation = backend.get_reservation(reservation_id, company_id)
    reservation_dict = reservation.to_dict()

    return reservation_dict


def get_all_reservations(company_id):
    reservations = backend.get_all_reservations(company_id)
    reservations_list = []
    for reservation in reservations:
        reservation_dict = reservation.to_dict()
        reservations_list.append(reservation_dict)

    return reservations_list


def update_reservation(reservation_data, reservation_id, company_id):
    reservation = backend.update_reservation(reservation_data, reservation_id, company_id)
    reservation_dict = reservation.to_dict()

    return reservation_dict


def delete_reservation(reservation_id, company_id):
    backend.delete_reservation(reservation_id, company_id)
