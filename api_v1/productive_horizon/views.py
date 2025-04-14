from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from core.models import db_helper
from .schemas import ProductiveHorizon, ProductiveHorizonCreate
from . import crud

router = APIRouter(prefix="/productive_horizon", tags=['reference_books', 'productive_horizon'])


@router.get('/all', response_model=list[ProductiveHorizon])
async def get_all_productive_horizon(session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.get_all_productive_horizon(session=session)


@router.get('/{productive_horizon_id}', response_model=ProductiveHorizon)
async def get_productive_horizon(productive_horizon_id: int, session: AsyncSession = Depends(db_helper.session_dependency)):
    horizon = await crud.get_productive_horizon(session=session, horizon_id=productive_horizon_id)
    if horizon is not None:
        return horizon

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Horizon {productive_horizon_id} not found!"  # строка, а не множество
    )


@router.post('/', response_model=ProductiveHorizon)
async def create_productive_horizon(horizon_in: ProductiveHorizonCreate,
                                    session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.create_productive_horizon(session=session, horizon_in=horizon_in)
