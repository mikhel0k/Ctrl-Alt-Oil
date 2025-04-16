from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from . import crud
from .schemas import TypeOfDevicesCreate, TypeOfDevices


router = APIRouter(prefix="/type_of_device", tags=['type_of_devices'])


@router.get("/all", response_model=list[TypeOfDevices])
async def get_all_types_of_devices(session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.get_all_types_of_devices(session=session)


@router.get("/{device_id}", response_model=TypeOfDevices)
async def get_type_of_device(device_id: int, session: AsyncSession = Depends(db_helper.session_dependency),):
    device = await crud.get_type_of_device(session=session, device_id=device_id)
    if device is None:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Device {device_id} not found!"
    )
    else:
        return device


@router.post("/", response_model=TypeOfDevices)
async def create_type_of_device(device_in: TypeOfDevicesCreate, session: AsyncSession = Depends(db_helper.session_dependency),):
    return await crud.create_type_of_device(session=session, device_in=device_in)
