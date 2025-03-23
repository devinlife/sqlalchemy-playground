import asyncio

from db import engine
from repository.models import Base


async def init_models():
    # 테이블을 생성 (migration이 아닌 직접 생성이 필요한 경우만 사용)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


if __name__ == "__main__":

    async def main():
        await init_models()  # 최초 1회 테이블 생성

    asyncio.run(main())
