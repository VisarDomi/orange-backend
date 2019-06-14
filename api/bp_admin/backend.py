from ..common.exceptions import (
    CannotChangeOthersData,
    CannotDeleteOthersData,
    CannotGetOthersData,
    CannotCreateData,
)
from ..models.users import Admin
from ..models.items import Invoice, Reservation
from ..helper_functions.get_entity_by_id import (
    get_admin_by_id,
    get_invoice_by_id,
    get_reservation_by_id,
    get_driver_by_id,
)
from ..helper_functions.common_functions import can_it_update
from ..helper_functions.crud_entity import create_entity


def create_admin(admin_data):
    can_update = can_it_update()
    if can_update:
        admin = create_entity(admin_data, Admin)
    else:
        msg = "You can't create admin."
        raise CannotCreateData(message=msg)

    return admin


def get_admins():
    can_update = can_it_update()
    if can_update:
        admins = Admin.query.all()
    else:
        msg = "You can't get admins."
        raise CannotGetOthersData(message=msg)

    return admins


def get_admin(admin_id):
    can_update = can_it_update()
    if can_update:
        admin = get_admin_by_id(admin_id)
    else:
        msg = "You can't get admins."
        raise CannotGetOthersData(message=msg)

    return admin


def update_admin(admin_data, admin_id):
    can_update = can_it_update()
    if can_update:
        admin = get_admin_by_id(admin_id)
        admin.update(**admin_data)
        admin.save()
    else:
        msg = "You can't change other people's data."
        raise CannotChangeOthersData(message=msg)

    return admin


def delete_admin(admin_id):
    can_update = can_it_update()
    if can_update:
        admin = get_admin_by_id(admin_id)
        admin.delete()
    else:
        msg = "You can't delete other people's data."
        raise CannotDeleteOthersData(message=msg)


def get_invoices():
    can_update = can_it_update()
    if can_update:
        invoices = Invoice.query.all()
    else:
        msg = "You can't get invoices."
        raise CannotGetOthersData(message=msg)

    return invoices


def get_invoice(invoice_id):
    can_update = can_it_update()
    if can_update:
        invoice = get_invoice_by_id(invoice_id)
    else:
        msg = "You can't get invoice."
        raise CannotGetOthersData(message=msg)

    return invoice


def get_reservations():
    can_update = can_it_update()
    if can_update:
        reservations = Reservation.query.all()
    else:
        msg = "You can't get reservations."
        raise CannotGetOthersData(message=msg)

    return reservations


def get_reservation(reservation_id):
    can_update = can_it_update()
    if can_update:
        reservation = get_reservation_by_id(reservation_id)
    else:
        msg = "You can't get reservation."
        raise CannotGetOthersData(message=msg)

    return reservation


def update_reservation(reservation_data, reservation_id):
    can_update = can_it_update()
    if can_update:
        driver_id = reservation_data.pop("driver_id")
        driver = get_driver_by_id(driver_id)
        reservation = get_reservation_by_id(reservation_id)
        reservation.status = "waiting"
        reservation.driver = driver
        reservation.save()
    else:
        msg = "You can't get reservation."
        raise CannotGetOthersData(message=msg)

    return reservation
