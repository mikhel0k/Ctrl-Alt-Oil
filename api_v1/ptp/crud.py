from sqlalchemy.ext.asyncio import  AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result
from datetime import datetime

from core.models import Ptp
from .schemas import PtpCreate, DateTimeFormatEnum

async def get_all_ptp(session: AsyncSession):
    stmt = select(Ptp).order_by(Ptp.id)
    result: Result = await session.execute(stmt)
    return result.scalars().all()

async def get_ptp(session: AsyncSession, ptp_id: int) -> Ptp | None:
    return await session.get(Ptp, ptp_id)


async def create_ptp(session: AsyncSession, ptp_in: PtpCreate) -> Ptp | None:
    data = ptp_in.model_dump()
    dt_format = data['DataTimeFormat']
    dt_value = data['DataTime']

    # Конвертация в ISO format
    if dt_format == DateTimeFormatEnum.ISO:
        iso_time = datetime.fromisoformat(dt_value).isoformat()
    elif dt_format == DateTimeFormatEnum.TIMESTAMP:
        iso_time = datetime.fromtimestamp(float(dt_value)).isoformat()
    elif dt_format == DateTimeFormatEnum.COUPON:
        date_part = dt_value.split('-')[0]
        iso_time = datetime.strptime(date_part, "%d%b%Y").isoformat()
    elif dt_format == DateTimeFormatEnum.CUSTOM:
        iso_time = datetime.strptime(dt_value, "%d-%m-%Y %H:%M").isoformat()
    elif dt_format == DateTimeFormatEnum.RAW:
        iso_time = dt_value  # Сохраняем как есть

    # Обновляем значение перед сохранением
    data['DataTime'] = iso_time

    ptp = Ptp(**data)
    session.add(ptp)
    await session.commit()
    await session.refresh(ptp)
    return ptp
