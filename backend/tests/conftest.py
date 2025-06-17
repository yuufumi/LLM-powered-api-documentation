import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.core.config import settings
from app.core.database import Base, get_db

# Use an in-memory SQLite for testing
TEST_DATABASE_URL = "sqlite+aiosqlite:///./test.db" # Or sqlite+aiosqlite:///:memory: for in-memory

@pytest.fixture(scope="session")
async def async_test_db_engine():
    engine = create_async_engine(TEST_DATABASE_URL, echo=True)
    yield engine
    # Optionally clean up the database file after tests are done
    # import os
    # if os.path.exists("./test.db"):
    #     os.remove("./test.db")

@pytest.fixture(scope="function")
async def async_test_session(async_test_db_engine):
    async with async_test_db_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    async_session_maker = sessionmaker(
        async_test_db_engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session_maker() as session:
        yield session
    async with async_test_db_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture(scope="function")
async def client(async_test_session):
    # Override the dependency for database in tests
    app.dependency_overrides[get_db] = lambda: async_test_session
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
    app.dependency_overrides.clear() # Clear overrides after test