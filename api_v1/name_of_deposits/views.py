from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from . import crud
from .schemas import NameOfDepositsCreate, NameOfDeposits


router = APIRouter(prefix="/name_of_deposits", tags=['name_of_deposits'])

@router.get("/all", response_model=list[NameOfDeposits])
async def get_all_name_of_devices(session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.get_all_name_of_deposits(session=session)

@router.post("/", response_model=list[NameOfDeposits])
async def create_name_of_deposit(deposit_in: NameOfDepositsCreate, session: AsyncSession = Depends(db_helper.session_dependency),):
    return await crud.create_name_of_deposit(session=session, deposit_in=deposit_in)

@router.get("/{deposit_id}", response_model=NameOfDeposits)
async def get_name_of_deposit(deposit_id: int, session: AsyncSession = Depends(db_helper.session_dependency),):
    deposit = await crud.get_name_of_deposit(session=session, deposit_id=deposit_id)
    if deposit is None:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Device {deposit_id} not found!"
    )
    else:
        return deposit
