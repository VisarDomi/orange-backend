from sqlalchemy.orm.exc import NoResultFound
from ..common.exceptions import RecordNotFound, InvalidURL
from ..common.models import (
    User,
    Admin,
    Driver,
    Employee,
    Company,
    Reservation,
    Invoice,
    Item,
)


def get_entity(entity_id, Entity):
    entity_name = "Entity"
    if Entity == User:
        entity_name = "User"
    if Entity == Admin:
        entity_name = "Admin"
    if Entity == Driver:
        entity_name = "Driver"
    if Entity == Employee:
        entity_name = "Employee"
    if Entity == Company:
        entity_name = "Company"
    if Entity == Reservation:
        entity_name = "Reservation"
    if Entity == Invoice:
        entity_name = "Invoice"
    if Entity == Item:
        entity_name = "Item"
    try:
        entity = Entity.query.filter(Entity.id == int(entity_id)).one()
    except NoResultFound:
        msg = f"There is no {entity_name} with id {entity_id}"
        raise RecordNotFound(message=msg)
    except (InvalidURL, ValueError):
        msg = f"This is not a valid URL: {entity_id}`"
        raise InvalidURL(message=msg)

    return entity


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
