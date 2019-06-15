from ..common.exceptions import (
    CannotChangeOthersData,
    CannotDeleteOthersData,
    CannotCreateData,
    CannotGetOthersData,
)
from ..models.items import Reservation, Stop
from ..helper_functions.get_entity_by_id import (
    get_employee_by_id,
    get_reservation_by_id,
    get_company_by_id,
    get_secretary_by_id,
    get_stop_by_id,
)
from ..helper_functions.common_functions import (
    can_it_update,
    is_it_head_secretary,
    get_secretary_id,
)
from ..helper_functions.constants import UNASSIGNED


def create_reservation(reservation_data, company_id):
    secretary_id = get_secretary_id(company_id)
    can_update = can_it_update(secretary_id=secretary_id)
    if can_update:
        stops_data = reservation_data.pop("stops")
        reservation_data["status"] = UNASSIGNED
        reservation = Reservation(**reservation_data)
        reservation.save()
        company = get_company_by_id(company_id)
        reservation.company = company
        if secretary_id:
            secretary = get_secretary_by_id(secretary_id)
            reservation.secretary = secretary
        for stop_data in stops_data:
            employee_id = stop_data.pop("employee_id")
            employee = get_employee_by_id(employee_id)
            stop = Stop(**stop_data)
            company = get_company_by_id(company_id)
            if employee in company.employees.all():
                stop.employee = employee
                stop.reservation = reservation
            stop.save()
        reservation.save()
    else:
        msg = f"You can't create data."
        raise CannotCreateData(message=msg)

    return reservation


def get_reservations(company_id):
    is_head_secretary = is_it_head_secretary(company_id)
    can_update = can_it_update()
    if can_update or is_head_secretary:
        company = get_company_by_id(company_id)
        reservations = company.reservations.all()
    else:
        msg = "You can't get reservations."
        raise CannotGetOthersData(message=msg)

    return reservations


def get_reservation(reservation_id, company_id):
    is_head_secretary = is_it_head_secretary(company_id)
    can_update = can_it_update()
    if can_update or is_head_secretary:
        reservation = get_reservation_by_id(reservation_id)
    else:
        msg = "You can't get reservation."
        raise CannotGetOthersData(message=msg)

    return reservation


def update_reservation(reservation_data, reservation_id, company_id):
    is_head_secretary = is_it_head_secretary(company_id)
    can_update = can_it_update()
    is_reservation_secretary = False
    secretary_id = get_secretary_id(company_id)
    secretary = get_secretary_by_id(secretary_id)
    reservation = get_reservation_by_id(reservation_id)
    if reservation.secretary == secretary:
        is_reservation_secretary = True
    if can_update or is_head_secretary or is_reservation_secretary:
        stops_data = []
        try:
            stops_data = reservation_data.pop("stops")
        except KeyError:
            pass
        reservation.update(**reservation_data)
        if stops_data:
            for stop_data in stops_data:
                stop_id = stop_data["id"]
                employee_id = stop_data["employee_id"]
                stop = get_stop_by_id(stop_id)
                employee = get_employee_by_id(employee_id)
                company = get_company_by_id(company_id)
                if employee in company.employees.all():
                    stop.employee = employee
                    stop.reservation = reservation
                    stop.update(**stop_data)
                    stop.save()
        reservation.save()
    else:
        msg = "You can't change other people's data."
        raise CannotChangeOthersData(message=msg)

    return reservation


def delete_reservation(reservation_id, company_id):
    is_head_secretary = is_it_head_secretary(company_id)
    can_update = can_it_update()
    is_reservation_secretary = False
    secretary_id = get_secretary_id(company_id)
    secretary = get_secretary_by_id(secretary_id)
    reservation = get_reservation_by_id(reservation_id)
    if reservation.secretary == secretary:
        is_reservation_secretary = True
    if can_update or is_head_secretary or is_reservation_secretary:
        reservation.delete()
    else:
        msg = "You can't delete other people's data."
        raise CannotDeleteOthersData(message=msg)
