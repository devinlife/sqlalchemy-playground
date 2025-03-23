from uuid import uuid4


from db import async_session
from domain.bucket import Bucket, BucketFile
from repository.bucket_repository import BucketRepository


async def create_bucket_file(bucket_name: str, file_key: str):

    async with async_session() as session:
        repo = BucketRepository(session)
        bucket = await repo.get_bucket(bucket_name)
        if not bucket:
            print(f"❌ Bucket with name {bucket_name} not found.")
            return

        file = BucketFile(id=bucket.id, s3_key=file_key)
        bucket.add_file(file)
        await repo.save(bucket)


async def create_bucket(name: str):
    bucket_id = uuid4()
    bucket = Bucket(id=bucket_id, name=name)

    async with async_session() as session:
        repo = BucketRepository(session)
        await repo.save(bucket)
        print(f"✅ Created bucket: id={bucket.id}, name={bucket.name}")


async def get_buckets():
    async with async_session() as session:
        repo = BucketRepository(session)
        buckets = await repo.list_buckets()

        for bucket in buckets:
            print(f" - ID: {bucket.id}, Name: {bucket.name}")

            if not bucket.files:
                print("   - No files found.")
                continue

            for file in bucket.files:
                print(f"   - File: {file.s3_key}")


async def get_bucket(bucket_name: int) -> Bucket | None:
    async with async_session() as session:
        repo = BucketRepository(session)
        bucket = await repo.get_bucket(bucket_name)
        if not bucket:
            print(f"❌ Bucket with ID {bucket_name} not found.")
            return

        return bucket


async def delete_bucket(bucket_id: int):
    async with async_session() as session:
        repo = BucketRepository(session)
        bucket = await repo.get_bucket(bucket_id)
        if not bucket:
            print(f"❌ Bucket with ID {bucket_id} not found.")
            return

        await session.delete(bucket)
        await session.commit()
        print(f"🗑️ Deleted bucket: id={bucket.id}, name={bucket.name}")
