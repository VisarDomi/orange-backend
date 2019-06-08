from . import backend


def create_itinerary_master(itinerary_master_data):
    itinerary_master = backend.create_itinerary_master(itinerary_master_data)
    itinerary_master_dict = itinerary_master.to_dict()

    return itinerary_master_dict


def get_itinerary_masters():
    itinerary_masters = backend.get_itinerary_masters()
    itinerary_masters_list = []
    for itinerary_master in itinerary_masters:
        itinerary_master_dict = itinerary_master.to_dict()
        itinerary_masters_list.append(itinerary_master_dict)

    return itinerary_masters_list


def get_itinerary_master(itinerary_master_id):
    itinerary_master = backend.get_itinerary_master(itinerary_master_id)
    itinerary_master_dict = itinerary_master.to_dict()

    return itinerary_master_dict


def update_itinerary_master(itinerary_master_data, itinerary_master_id):
    itinerary_master = backend.update_itinerary_master(itinerary_master_data, itinerary_master_id)
    itinerary_master_dict = itinerary_master.to_dict()

    return itinerary_master_dict


def delete_itinerary_master(itinerary_master_id):
    backend.delete_itinerary_master(itinerary_master_id)
