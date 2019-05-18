from . import backend
from ..helper_functions.get_by_id import get_trip_by_id as backend_get_trip_by_id


def create_trip(trip_data, user_id):
    trip = backend.create_trip(trip_data, user_id)
    trip_dict = trip.to_dict()

    return trip_dict


def get_trip_by_id(trip_id):
    trip = backend_get_trip_by_id(trip_id)
    trip_dict = trip.to_dict()

    return trip_dict


def get_all_trips(user_id):
    trips = backend.get_all_trips(user_id)
    trips_list = []
    for trip in trips:
        trip_dict = trip.to_dict()
        trips_list += [trip_dict]

    return trips_list


def update_trip(trip_data, user_id, trip_id):
    trip = backend.update_trip(trip_data, user_id, trip_id)
    trip_dict = trip.to_dict()

    return trip_dict


def delete_trip(user_id, trip_id):
    backend.delete_trip(user_id, trip_id)
