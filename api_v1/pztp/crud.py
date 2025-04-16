from sqlalchemy.ext.asyncio import  AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result

from core.datetime_utils import convert_to_iso
from core.models import Pztp
from .schemas import PztpCreate

async def get_all_pztp(session: AsyncSession):
    stmt = select(Pztp).order_by(Pztp.id)
    result: Result = await session.execute(stmt)
    return result.scalars().all()

async def get_pztp(session: AsyncSession, pztp_id: int) -> Pztp | None:
    return await session.get(Pztp, pztp_id)


async def create_ptp(session: AsyncSession, pztp_in: PztpCreate) -> Pztp | None:
    data = pztp_in.model_dump()
    data['DataTime'] =convert_to_iso(dt_value=data['DataTime'], dt_format=data['DataTimeFormat'])
    pztp = Pztp(**data)
    session.add(pztp)
    await session.commit()
    await session.refresh(pztp)
    return pztp
