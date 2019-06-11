from . import backend
from ..helper_functions.dict import reservation_to_dict


def create_secretary(secretary_data, company_id):
    secretary = backend.create_secretary(secretary_data, company_id)
    secretary_dict = secretary.to_dict()

    return secretary_dict


def get_secretarys(company_id):
    secretarys = backend.get_secretarys(company_id)
    secretarys_list = []
    for secretary in secretarys:
        secretary_dict = secretary.to_dict()
        secretarys_list.append(secretary_dict)

    return secretarys_list


def get_secretary(secretary_id, company_id):
    secretary = backend.get_secretary(secretary_id, company_id)
    secretary_dict = secretary.to_dict()

    return secretary_dict


def update_secretary(secretary_data, secretary_id, company_id):
    secretary = backend.update_secretary(secretary_data, secretary_id, company_id)
    secretary_dict = secretary.to_dict()

    return secretary_dict


def delete_secretary(secretary_id, company_id):
    backend.delete_secretary(secretary_id, company_id)


def get_reservations(secretary_id, company_id):
    reservations = backend.get_reservations(secretary_id, company_id)
    reservation_list = []
    for reservation in reservations:
        reservation_dict = reservation_to_dict(reservation)
        reservation_list.append(reservation_dict)

    return reservation_list


def get_reservation(secretary_id, company_id, reservation_id):
    reservation = backend.get_reservation(secretary_id, company_id, reservation_id)
    reservation_dict = reservation_to_dict(reservation)

    return reservation_dict
