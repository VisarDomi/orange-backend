from flask import g
from ..common.exceptions import (
    CannotChangeOthersData,
    CannotDeleteOthersData,
)
from ..common.models import Company
from ..helper_functions.create import create_entity
from ..helper_functions.get_by_id import get_company_by_id


def create_company(company_data):
    company = create_entity(company_data, Company)

    return company


def get_all_companys():
    companys = Company.query.all()

    return companys


def update_company(company_data, company_id):
    try:
        if int(company_id) == g.current_user.company.id:
            company = get_company_by_id(company_id)
            company.update(**company_data)
            company.save()
        else:
            msg = "You can't change other people's data."
            raise CannotChangeOthersData(message=msg)
    except AttributeError:
        msg = "AttributeError, You can't change other people's data."
        raise CannotChangeOthersData(message=msg)

    return company


def delete_company(company_id):
    try:
        if int(company_id) == g.current_user.company.id:
            company = get_company_by_id(company_id)
            company.delete()
        else:
            msg = "You can't delete other people's data."
            raise CannotDeleteOthersData(message=msg)
    except AttributeError:
        msg = "AttributeError, You can't change other people's data."
        raise CannotChangeOthersData(message=msg)
