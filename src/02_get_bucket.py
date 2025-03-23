import asyncio

from usecase.bucket import get_bucket

if __name__ == "__main__":

    async def main():
        name = "test"
        bucket = await get_bucket(name)
        print(bucket)

    asyncio.run(main())
