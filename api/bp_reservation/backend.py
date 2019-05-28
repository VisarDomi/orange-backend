from flask import g
from ..common.exceptions import (
    CannotChangeOthersData,
    CannotDeleteOthersData,
)
from ..common.models import Reservation
from ..helper_functions.get_by_id import get_reservation_by_id


def create_reservation(reservation_data):
    reservation = Reservation(**reservation_data)
    reservation.save()

    return reservation


def get_all_reservations():
    reservations = Reservation.query.all()

    return reservations


def update_reservation(reservation_data, reservation_id):
    if int(reservation_id) == g.current_user.id:
        reservation = get_reservation_by_id(reservation_id)
        reservation.update(**reservation_data)
        reservation.save()
    else:
        msg = "You can't change other people's data."
        raise CannotChangeOthersData(message=msg)

    return reservation


def delete_reservation(reservation_id):
    if int(reservation_id) == g.current_user.id:
        reservation = get_reservation_by_id(reservation_id)
        reservation.delete()
    else:
        msg = "You can't delete other people's data."
        raise CannotDeleteOthersData(message=msg)
