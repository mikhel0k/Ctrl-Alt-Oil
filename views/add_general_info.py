from fastapi import APIRouter

from schemas.general_info import ProductiveHorizon, NameOfDeposits, TypeOfDevices


router = APIRouter(prefix="/add/reference_books", tags=['reference_books'])


@router.post('/productive_horizon')
def productive_horizon(data: ProductiveHorizon):
    return data


@router.post('/name_of_deposits')
def name_of_deposits(data: NameOfDeposits):
    return data

@router.post('/type_of_devices')
def type_of_devices(data: TypeOfDevices):
    return data
