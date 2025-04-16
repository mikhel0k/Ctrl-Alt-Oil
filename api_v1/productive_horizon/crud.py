from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import ProductiveHorizon
from .schemas import ProductiveHorizonCreate


async def get_all_productive_horizon(session: AsyncSession):
    stmt = select(ProductiveHorizon).order_by(ProductiveHorizon.id)
    result: Result = await session.execute(stmt)
    return result.scalars().all()


async def get_productive_horizon(session: AsyncSession, horizon_id: int) -> ProductiveHorizon | None:
    return await session.get(ProductiveHorizon, horizon_id)


async def create_productive_horizon(session: AsyncSession, horizon_in: ProductiveHorizonCreate) -> ProductiveHorizon | None:
    horizon = ProductiveHorizon(**horizon_in.model_dump())
    session.add(horizon)
    await session.commit()
    return horizon
