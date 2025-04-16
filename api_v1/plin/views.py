from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from . import crud
from .schemas import PlinCreate, Plin

router = APIRouter(prefix="/plin", tags=["plin"])

@router.get('/all', response_model=list[Plin])
async def get_all_plin(session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.get_all_plin(session=session)


@router.get('/{plin_id}', response_model=Plin)
async def get_ptp(plin_id: int, session: AsyncSession = Depends(db_helper.session_dependency)):
    plin = await crud.get_plin(session=session, plin_id=plin_id)
    if plin is not None:
        return plin

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Plin {plin_id} not found!"  # строка, а не множество
    )


@router.post('/', response_model=Plin)
async def create_ptp(plin_in: PlinCreate, session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.create_ptp(session=session, plin_in=plin_in)