from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from repository.models import OrmDataset


class DatasetRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_dataset(self, dataset_id: int) -> OrmDataset | None:
        return await self.session.get(OrmDataset, dataset_id)

    async def create_dataset(self, name: str, s3_keys: list[str]) -> OrmDataset:
        dataset = OrmDataset(name=name, files=s3_keys)
        self.session.add(dataset)
        await self.session.commit()
        await self.session.refresh(dataset)
        return dataset

    async def list_datasets(self) -> list[OrmDataset]:
        query = select(OrmDataset)
        result = await self.session.execute(query)
        return result.scalars().all()
