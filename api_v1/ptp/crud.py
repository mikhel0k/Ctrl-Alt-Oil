from sqlalchemy.ext.asyncio import  AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result

from core.datetime_utils import convert_to_iso
from core.models import Ptp
from .schemas import PtpCreate

async def get_all_ptp(session: AsyncSession):
    stmt = select(Ptp).order_by(Ptp.id)
    result: Result = await session.execute(stmt)
    return result.scalars().all()

async def get_ptp(session: AsyncSession, ptp_id: int) -> Ptp | None:
    return await session.get(Ptp, ptp_id)


async def create_ptp(session: AsyncSession, ptp_in: PtpCreate) -> Ptp | None:
    data = ptp_in.model_dump()
    data['DataTime'] =convert_to_iso(dt_value=data['DataTime'], dt_format=data['DataTimeFormat'])
    ptp = Ptp(**data)
    session.add(ptp)
    await session.commit()
    await session.refresh(ptp)
    return ptp
