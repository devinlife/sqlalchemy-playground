from faker import Faker

from db import async_session
from domain.bucket import Bucket, BucketFile
from repository.bucket_repository import BucketRepository


async def add_file_to_bucket(bucket_id: int, file: BucketFile):
    async with async_session() as session:
        repo = BucketRepository(session)
        bucket = await repo.get_bucket(bucket_id)
        if not bucket:
            print(f"❌ Bucket with ID {bucket_id} not found.")
            return

        bucket.add_file(file)
        await repo.save(bucket)


async def create_bucket(name: str | None = None):
    if not name:
        fake = Faker()
        name = fake.name()

    bucket = Bucket(id=1, name=name)

    async with async_session() as session:
        repo = BucketRepository(session)
        bucket = await repo.create_bucket(name)
        print(f"✅ Created bucket: id={bucket.id}, name={bucket.name}")


async def list_buckets():
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


async def get_bucket(bucket_id: int):
    async with async_session() as session:
        repo = BucketRepository(session)
        bucket = await repo.get_bucket(bucket_id)
        if not bucket:
            print(f"❌ Bucket with ID {bucket_id} not found.")
            return

        print(f"📦 Bucket ID: {bucket.id}, Name: {bucket.name}")
        if not bucket.files:
            print("   - No files.")
        else:
            for file in bucket.files:
                print(f"   - File: {file.s3_key}")


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
