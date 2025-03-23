import asyncio

from faker import Faker

from usecase.bucket import create_bucket

if __name__ == "__main__":

    async def main():
        name = "test"

        if not name:
            fake = Faker()
            name = fake.name()

        await create_bucket(name)

    asyncio.run(main())
