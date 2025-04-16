from sqlalchemy.ext.asyncio import  AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result
from api_v1.research.schemas import ResearchCreate
from core.models import Research


async def get_all_researches(session: AsyncSession):
    query = select(Research).order_by(Research.id)
    result: Result = await session.execute(query)
    return result.scalars().all()

async def get_research(session: AsyncSession, research_id: int) -> Research | None:
    return await session.get(Research, research_id)

async def get_id_field_time(session: AsyncSession):
    query = select(Research.id, Research.field, Research.research_start_date, Research.research_end_date).order_by(Research.id)
    result: Result = await session.execute(query)
    return result.all()

async def create_research(session: AsyncSession, research_in: ResearchCreate) -> Research | None:
    research = Research(**research_in.model_dump())
    session.add(research)
    await session.commit()
    return research
