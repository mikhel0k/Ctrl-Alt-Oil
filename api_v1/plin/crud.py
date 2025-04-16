from sqlalchemy.ext.asyncio import  AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result

from core.datetime_utils import convert_to_iso
from core.models import Plin
from .schemas import PlinCreate

async def get_all_plin(session: AsyncSession):
    stmt = select(Plin).order_by(Plin.id)
    result: Result = await session.execute(stmt)
    return result.scalars().all()

async def get_plin(session: AsyncSession, plin_id: int) -> Plin | None:
    return await session.get(Plin, plin_id)


async def create_ptp(session: AsyncSession, plin_in: PlinCreate) -> Plin | None:
    data = plin_in.model_dump()
    data['DataTime'] =convert_to_iso(dt_value=data['DataTime'], dt_format=data['DataTimeFormat'])
    plin = Plin(**data)
    session.add(plin)
    await session.commit()
    await session.refresh(plin)
    return plin
