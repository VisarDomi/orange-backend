from . import backend


def create_itinerary(itinerary_data, company_id):
    itinerary = backend.create_itinerary(itinerary_data, company_id)
    itinerary_dict = itinerary.to_dict()

    return itinerary_dict


def get_itinerarys(company_id):
    itinerarys = backend.get_itinerarys(company_id)
    itinerarys_list = []
    for itinerary in itinerarys:
        itinerary_dict = itinerary.to_dict()
        itinerarys_list.append(itinerary_dict)

    return itinerarys_list


def get_itinerary(itinerary_id, company_id):
    itinerary = backend.get_itinerary(itinerary_id, company_id)
    itinerary_dict = itinerary.to_dict()

    return itinerary_dict


def update_itinerary(itinerary_data, itinerary_id, company_id):
    itinerary = backend.update_itinerary(itinerary_data, itinerary_id, company_id)
    itinerary_dict = itinerary.to_dict()

    return itinerary_dict


def delete_itinerary(itinerary_id, company_id):
    backend.delete_itinerary(itinerary_id, company_id)
