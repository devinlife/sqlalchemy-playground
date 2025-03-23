import asyncio

from db import engine
from repository.models import Base
from usecase.bucket import create_bucket, get_bucket, get_buckets

# async def list_buckets():
#     async with async_session() as session:
#         repo = bucket_repository.BucketRepository(session)
#         buckets = await repo.list_buckets()

#         if not buckets:
#             print("📭 No buckets found.")
#             return

#         print("📦 List of Buckets:")
#         for bucket in buckets:
#             print(f" - ID: {bucket.id}, Name: {bucket.name}")
#             for file in bucket.files:
#                 print(f"   - File: {file.s3_key}")


async def init_models():
    # 테이블을 생성 (migration이 아닌 직접 생성이 필요한 경우만 사용)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


if __name__ == "__main__":

    async def main():
        # await init_models()  # 최초 1회 테이블 생성

        # print(bucket_file)

        if False:
            bucket = await get_bucket(1)
            print(bucket)
            await get_bucket(1)
            await get_buckets()
            await create_bucket()

    asyncio.run(main())
