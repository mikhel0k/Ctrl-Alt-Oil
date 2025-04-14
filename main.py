from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
import uvicorn

from core.models import db_helper, Base
from views.add_measurements import router as add_measurements_router
from views.add_general_info import router as add_general_information_router


@asynccontextmanager
async def lifespan(app:FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield

app = FastAPI(lifespan=lifespan)
app.include_router(add_measurements_router)
app.include_router(add_general_information_router)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
