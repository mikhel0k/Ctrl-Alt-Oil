from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from . import crud
from .schemas import PztpCreate, Pztp

router = APIRouter(prefix="/pztp", tags=["pztp"])

@router.get('/all', response_model=list[Pztp])
async def get_all_pztp(session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.get_all_pztp(session=session)


@router.get('/{pztp_id}', response_model=Pztp)
async def get_ptp(pztp_id: int, session: AsyncSession = Depends(db_helper.session_dependency)):
    pztp = await crud.get_pztp(session=session, pztp_id=pztp_id)
    if pztp is not None:
        return pztp

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Horizon {pztp_id} not found!"  # строка, а не множество
    )


@router.post('/', response_model=Pztp)
async def create_ptp(pztp_in: PztpCreate, session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.create_ptp(session=session, pztp_in=pztp_in)