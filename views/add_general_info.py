from fastapi import APIRouter

from schemas.general_info import ProductiveHorizon, NameOfDeposits, TypeOfDevices
from CRUD.crud_general_info import add_productive_horizon, add_name_of_deposits, add_type_of_devices


router = APIRouter(prefix="/add/reference_books", tags=['reference_books'])


@router.post('/productive_horizon')
def productive_horizon(data: ProductiveHorizon):
    return add_productive_horizon(data)


@router.post('/name_of_deposits')
def name_of_deposits(data: NameOfDeposits):
    return add_name_of_deposits(data)


@router.post('/type_of_devices')
def type_of_devices(data: TypeOfDevices):
    return add_type_of_devices(data)
