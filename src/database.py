from typing import AsyncGenerator
from sqlalchemy import NullPool
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from src.config import DATABASE_URL



engine = create_async_engine(DATABASE_URL)

async_session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        try:
            yield session
        finally:
            await session.close()


async def get_db_generator() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session