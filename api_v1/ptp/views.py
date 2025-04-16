from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from . import crud
from .schemas import PtpCreate, Ptp

router = APIRouter(prefix="/ptp", tags=["ptp"])

@router.get('/all', response_model=list[Ptp])
async def get_all_ptp(session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.get_all_ptp(session=session)


@router.get('/{ptp_id}', response_model=Ptp)
async def get_ptp(ptp_id: int, session: AsyncSession = Depends(db_helper.session_dependency)):
    ptp = await crud.get_ptp(session=session, ptp_id=ptp_id)
    if ptp is not None:
        return ptp

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Ptp {ptp_id} not found!"  # строка, а не множество
    )


@router.post('/', response_model=Ptp)
async def create_ptp(ptp_in: PtpCreate, session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.create_ptp(session=session, ptp_in=ptp_in)