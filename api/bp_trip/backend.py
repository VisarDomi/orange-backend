from flask import g
from ..common.exceptions import (
    CannotChangeOthersData,
    CannotDeleteOthersData,
)
from ..common.models import Trip
from ..helper_functions.get_by_id import get_trip_by_id


def create_trip(trip_data, user_id):
    if int(user_id) == g.current_user.id:
        trip = Trip(**trip_data)
        trip.driver = g.current_user
        trip.save()
    else:
        msg = f"You can't change other people's data."
        raise CannotChangeOthersData(message=msg)

    return trip


def get_all_trips(user_id):
    trips = Trip.query.filter(Trip.driver_id == user_id).all()

    return trips


def update_trip(trip_data, user_id, trip_id):
    if int(user_id) == g.current_user.id:
        trip = get_trip_by_id(trip_id)
        trip.update(**trip_data)
        trip.save()
    else:
        msg = f"You can't change other people's data."
        raise CannotChangeOthersData(message=msg)

    return trip


def delete_trip(user_id, trip_id):
    if int(user_id) == g.current_user.id:
        trip = get_trip_by_id(trip_id)
        trip.delete()
    else:
        msg = "You can't delete other people's data."
        raise CannotDeleteOthersData(message=msg)
