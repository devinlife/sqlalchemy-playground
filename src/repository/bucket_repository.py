from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from domain.bucket import BucketFile, Bucket
from repository.models import OrmBucket, OrmBucketFile


class BucketRepository:
    def __init__(self, session: AsyncSession):
        self.session = session
   
    async def save(self, bucket: Bucket) -> None:
        orm_bucket = OrmBucket.to_orm(bucket)
        self.session.add(orm_bucket)
        await self.session.commit()

    async def get_bucket(self, bucket_id: int) -> Bucket | None:
        query = select(OrmBucket).where(OrmBucket.id == bucket_id)
        result = await self.session.execute(query)
        orm_bucket = result.scalar_one_or_none()
        if orm_bucket:
            # return Bucket.from_orm(orm_bucket)
            return OrmBucket.from_orm(orm_bucket)
        return None

    async def get_bucket_with_files(self, bucket_id: int) -> OrmBucket | None:
        stmt = select(OrmBucket).options(selectinload(OrmBucket.files)).where(OrmBucket.id == bucket_id)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def create_bucket(self, name: str) -> OrmBucket:
        bucket = OrmBucket(name=name)
        self.session.add(bucket)
        await self.session.commit()
        await self.session.refresh(bucket)
        return bucket

    async def list_buckets(self) -> list[OrmBucket]:
        query = select(OrmBucket)
        result = await self.session.execute(query)
        return result.scalars().all()

    async def add_file_to_bucket(self, bucket_id: int, file: BucketFile) -> OrmBucketFile:
        bucket = await self.get_bucket(bucket_id)
        if not bucket:
            raise ValueError(f"Bucket #{bucket_id} not found.")

        file = OrmBucketFile(bucket_id=bucket.id, s3_key=s3_key)
        self.session.add(file)
        await self.session.commit()
        await self.session.refresh(file)
        return file
