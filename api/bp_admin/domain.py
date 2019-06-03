from . import backend


def create_admin(admin_data):
    admin = backend.create_admin(admin_data)
    admin_dict = admin.to_dict()

    return admin_dict


def get_admins():
    admins = backend.get_admins()
    admins_list = []
    for admin in admins:
        admin_dict = admin.to_dict()
        admins_list.append(admin_dict)

    return admins_list


def get_admin(admin_id):
    admin = backend.get_admin(admin_id)
    admin_dict = admin.to_dict()

    return admin_dict


def update_admin(admin_data, admin_id):
    admin = backend.update_admin(admin_data, admin_id)
    admin_dict = admin.to_dict()

    return admin_dict


def delete_admin(admin_id):
    backend.delete_admin(admin_id)


def get_invoices():
    invoices = backend.get_invoices()
    invoices_list = []
    for invoice in invoices:
        invoice_dict = invoice.to_dict()
        invoices_list.append(invoice_dict)

    return invoices_list


def get_invoice(invoice_id):
    invoice = backend.get_invoice(invoice_id)
    invoice_dict = invoice.to_dict()
    items = invoice.items.all()
    invoice_dict["items"] = []
    for item in items:
        item_dict = item.to_dict()
        invoice_dict["items"].append(item_dict)

    return invoice_dict


def get_reservations():
    reservations = backend.get_reservations()
    reservations_list = []
    for reservation in reservations:
        reservation_dict = reservation.to_dict()
        employees = []
        for employee in reservation.employees.all():
            employees.append(employee.to_dict())
        if reservation.company:
            reservation_dict["company"] = reservation.company.to_dict()
        else:
            reservation_dict["company"] = {}
        if reservation.driver:
            reservation_dict["driver"] = reservation.driver.to_dict()
        else:
            reservation_dict["driver"] = {}
        reservation_dict["employees"] = employees
        reservations_list.append(reservation_dict)

    return reservations_list


def get_reservation(reservation_id):
    reservation = backend.get_reservation(reservation_id)
    reservation_dict = reservation.to_dict()
    employees = []
    for employee in reservation.employees.all():
        employees.append(employee.to_dict())
    if reservation.company:
        reservation_dict["company"] = reservation.company.to_dict()
    else:
        reservation_dict["company"] = {}
    if reservation.driver:
        reservation_dict["driver"] = reservation.driver.to_dict()
    else:
        reservation_dict["driver"] = {}
    reservation_dict["employees"] = employees

    return reservation_dict


def update_reservation(reservation_data, reservation_id):
    reservation = backend.update_reservation(reservation_data, reservation_id)
    reservation_dict = reservation.to_dict()
    employees = []
    for employee in reservation.employees.all():
        employees.append(employee.to_dict())
    if reservation.company:
        reservation_dict["company"] = reservation.company.to_dict()
    else:
        reservation_dict["company"] = {}
    if reservation.driver:
        reservation_dict["driver"] = reservation.driver.to_dict()
    else:
        reservation_dict["driver"] = {}
    reservation_dict["employees"] = employees

    return reservation_dict
