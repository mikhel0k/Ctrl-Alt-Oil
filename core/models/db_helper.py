from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, async_scoped_session
from sqlalchemy.orm import sessionmaker
from asyncio import current_task

from core.config import settings


class DatabaseHelper:
    def __init__(self, url, echo: bool = False):
        self.engine = create_async_engine(
            url=url,
            echo=echo,
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autocommit=False,
            autoflush=False,
            expire_on_commit=False
        )


    def get_scoped_session(self):
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task,
        )
        return session


    async def session_dependency(self):
        async with self.get_scoped_session() as session:
            yield session
            await session.remove()


db_helper = DatabaseHelper(url=settings.db_url, echo=settings.db_echo)
