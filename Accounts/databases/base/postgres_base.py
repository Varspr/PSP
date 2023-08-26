from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from Accounts.databases.config import config

database_url = f"postgresql+asyncpg://{config.login}:{config.password}@{config.host}:{config.port}/{config.database}"
engine = create_async_engine(database_url)
async_session = async_sessionmaker(engine=engine, expire_on_commit=False)
meta = MetaData()
