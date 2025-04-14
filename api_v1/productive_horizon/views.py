from fastapi import APIRouter, HTTPException, status
from sqlalchemy.orm import Session

from .schemas import ProductiveHorizon, ProductiveHorizonCreate
from . import crud

router = APIRouter(prefix="/add/loading/productive_horizon", tags=['reference_books', 'productive_horizon'])


@router.get('/all', response_model=list[ProductiveHorizon])
async def get_all_productive_horizon(session):
    return await crud.get_all_productive_horizon(session=session)


@router.get('/{productive_horizon_id}', response_model=ProductiveHorizon)
async def get_productive_horizon(session, productive_horizon_id: int):
    horizon = await crud.create_productive_horizon(session=session, horizon_in=horizon_in)
    if horizon is not None:
        return horizon

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail = {f"Horizon {horizon} not found!"}
        )


@router.post('/', response_model=ProductiveHorizon)
async def create_productive_horizon(session, horizon_in: ProductiveHorizonCreate):
    return await crud.create_productive_horizon(session=session, horizon_in=horizon_in)
