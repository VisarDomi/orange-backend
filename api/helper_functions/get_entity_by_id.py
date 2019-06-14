from ..models.users import User, Admin, Driver, Employee, Secretary
from ..models.items import (
    Company,
    Reservation,
    Invoice,
    Item,
    Itinerary,
    ItineraryMaster,
    Stop,
)
from .crud_entity import get_entity


# models.users
def get_user_by_id(user_id):
    user = get_entity(user_id, User)

    return user


def get_admin_by_id(admin_id):
    admin = get_entity(admin_id, Admin)

    return admin


def get_driver_by_id(driver_id):
    driver = get_entity(driver_id, Driver)

    return driver


def get_employee_by_id(employee_id):
    employee = get_entity(employee_id, Employee)

    return employee


def get_secretary_by_id(secretary_id):
    secretary = get_entity(secretary_id, Secretary)

    return secretary


# models.items
def get_company_by_id(company_id):
    company = get_entity(company_id, Company)

    return company


def get_reservation_by_id(reservation_id):
    reservation = get_entity(reservation_id, Reservation)

    return reservation


def get_invoice_by_id(invoice_id):
    invoice = get_entity(invoice_id, Invoice)

    return invoice


def get_item_by_id(item_id):
    item = get_entity(item_id, Item)

    return item


def get_itinerary_by_id(itinerary_id):
    itinerary = get_entity(itinerary_id, Itinerary)

    return itinerary


def get_itinerary_master_by_id(itinerary_master_id):
    itinerary_master = get_entity(itinerary_master_id, ItineraryMaster)

    return itinerary_master


def get_stop_by_id(stop_id):
    stop = get_entity(stop_id, Stop)

    return stop
