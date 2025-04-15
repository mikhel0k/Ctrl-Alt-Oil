from sqlalchemy.ext.asyncio import  AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result

from core.models import TypeOfDevices
from .schemas import TypeOfDevicesCreate

async def get_all_types_of_devices(session: AsyncSession):
    stmt = select(TypeOfDevices).order_by(TypeOfDevices.id)
    result: Result = await session.execute(stmt)
    return result.scalars().all()

async def get_type_of_device(session: AsyncSession, device_id: int) -> TypeOfDevices | None:
    return await session.get(TypeOfDevices, device_id)


async def create_type_of_device(session: AsyncSession, device_in: TypeOfDevicesCreate) -> TypeOfDevices | None:
    device = TypeOfDevices(**device_in.model_dump())
    session.add(device)
    await session.commit()
    return device