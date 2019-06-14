def reservation_to_dict(reservation):
    reservation_dict = reservation.to_dict()
    stop_list = []
    stops = reservation.stops.all()
    if reservation.company:
        reservation_dict["company"] = reservation.company.to_dict()
    else:
        reservation_dict["company"] = {}
    if reservation.driver:
        reservation_dict["driver"] = reservation.driver.to_dict()
    else:
        reservation_dict["driver"] = {}
    for stop in stops:
        employee = stop.employee
        stop_dict = stop.to_dict()
        stop_dict["employee_full_name"] = employee.full_name
        stop_list.append(stop_dict)
    reservation_dict["stops"] = stop_list

    return reservation_dict


def invoice_to_dict(invoice):
    invoice_dict = invoice.to_dict()
    items = invoice.items.all()
    invoice_dict["items"] = []
    for item in items:
        item_dict = item.to_dict()
        invoice_dict["items"].append(item_dict)
    if invoice.reservation.destination:
        invoice_dict["destination"] = invoice.reservation.destination
    else:
        invoice_dict["destination"] = ""

    return invoice_dict
