from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from os import getenv
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = getenv("DATABASE_URL")

engine = create_async_engine(DATABASE_URL)

async_session = async_sessionmaker(
    bind=engine, expire_on_commit=False, class_=AsyncSession
)