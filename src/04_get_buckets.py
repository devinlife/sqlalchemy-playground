import asyncio

from usecase.bucket import get_buckets

if __name__ == "__main__":

    async def main():
        await get_buckets()

    asyncio.run(main())
