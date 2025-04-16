from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result

from core.models import NameOfDeposits
from .schemas import NameOfDepositsCreate

async def get_all_name_of_deposits(session: AsyncSession) -> list[NameOfDeposits]:
    stmt = select(NameOfDeposits).order_by(NameOfDeposits.id)
    result: Result = await session.execute(stmt)
    return list(result.scalars().all())

async def get_name_of_deposit(session: AsyncSession, deposit_id: int) -> NameOfDeposits | None:
    return await session.get(NameOfDeposits, deposit_id)

async def create_name_of_deposit(session: AsyncSession, deposit_in: NameOfDepositsCreate) -> NameOfDeposits | None:
    deposit = NameOfDeposits(**deposit_in.model_dump())
    session.add(deposit)
    await session.commit()
    return deposit