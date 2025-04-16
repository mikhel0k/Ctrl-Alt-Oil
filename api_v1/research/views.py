from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from . import crud
from .schemas import ResearchCreate, Research, ResearchFour

router = APIRouter(prefix="/research", tags=['research'])


@router.get("/all", response_model=list[Research])
async def get_all_researches(session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.get_all_researches(session=session)

@router.get("/all_four", response_model=list[ResearchFour])
async def get_id_field_time(session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.get_id_field_time(session=session)

@router.get("/{research_id}", response_model=Research)
async def get_research(research_id: int, session: AsyncSession = Depends(db_helper.session_dependency),):
    research = await crud.get_research(session=session, research_id=research_id)
    if research is None:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Research {research} not found!"
    )
    else:
        return research

@router.post("/", response_model=Research)
async def create_research(research_in: ResearchCreate, session: AsyncSession = Depends(db_helper.session_dependency),):
    return await crud.create_research(session=session, research_in=research_in)


