import asyncio
import sys
from faker import Faker
from db import async_session
from repository.models import OrmBucket, OrmBucketFile

faker = Faker()


async def create_bucket_files(bucket_id: int, count: int):
    async with async_session() as session:
        bucket: OrmBucket = await session.get(OrmBucket, bucket_id)
        if not bucket:
            print(f"❌ Bucket with id {bucket_id} not found.")
            return

        for _ in range(count):
            s3_key = f"{faker.file_path(depth=3, category='image')}"
            file = OrmBucketFile(bucket_id=bucket_id, s3_key=s3_key)
            bucket.files.append(file)
            session.add(file)

        await session.commit()

        print(f"✅ Created {count} bucket files in bucket #{bucket_id}")
        for file in files:
            print(f" - s3_key: {file.s3_key}")


if __name__ == "__main__":
    bucket_id = 1
    count = 10

    asyncio.run(create_bucket_files(bucket_id, count))
