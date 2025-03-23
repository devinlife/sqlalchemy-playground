from typing import List

from sqlalchemy import ForeignKey, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from domain.bucket import Bucket, BucketFile


class Base(DeclarativeBase):
    pass


class OrmBucket(Base):
    __tablename__ = "buckets"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    files: Mapped[List["OrmBucketFile"]] = relationship(cascade="all, delete-orphan", lazy="selectin")

    @classmethod
    def from_orm(cls, orm_bucket: "OrmBucket") -> Bucket:
        return Bucket(
            id=orm_bucket.id, name=orm_bucket.name, files=[OrmBucketFile.from_orm(file) for file in orm_bucket.files]
        )

    @staticmethod
    def to_orm(bucket: Bucket) -> "OrmBucket":
        return OrmBucket(
            id=str(bucket.id), name=bucket.name, files=[OrmBucketFile.to_orm(file) for file in bucket.files]
        )


class OrmBucketFile(Base):
    __tablename__ = "bucket_files"

    id: Mapped[str] = mapped_column(primary_key=True)
    bucket_id: Mapped[str] = mapped_column(ForeignKey("buckets.id"))
    s3_key: Mapped[str] = mapped_column(String(200))

    @classmethod
    def from_orm(cls, orm_bucket_file: "OrmBucketFile") -> "BucketFile":
        return BucketFile(id=orm_bucket_file.id, s3_key=orm_bucket_file.s3_key)

    @staticmethod
    def to_orm(bucket_file: BucketFile) -> "OrmBucketFile":
        return OrmBucketFile(id=str(bucket_file.id), bucket_id=1, s3_key=bucket_file.s3_key)


class OrmDataset(Base):
    __tablename__ = "datasets"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    files: Mapped[List[str]] = mapped_column(JSONB)
