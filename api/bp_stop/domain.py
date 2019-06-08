from . import backend


def create_stop(stop_data):
    stop = backend.create_stop(stop_data)
    stop_dict = stop.to_dict()

    return stop_dict


def get_stops():
    stops = backend.get_stops()
    stops_list = []
    for stop in stops:
        stop_dict = stop.to_dict()
        stops_list.append(stop_dict)

    return stops_list


def get_stop(stop_id):
    stop = backend.get_stop(stop_id)
    stop_dict = stop.to_dict()

    return stop_dict


def update_stop(stop_data, stop_id):
    stop = backend.update_stop(stop_data, stop_id)
    stop_dict = stop.to_dict()

    return stop_dict


def delete_stop(stop_id):
    backend.delete_stop(stop_id)
