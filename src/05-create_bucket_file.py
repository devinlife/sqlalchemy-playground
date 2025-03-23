import asyncio

from faker import Faker

from usecase.bucket import create_bucket_file

if __name__ == "__main__":

    async def main():
        bucket_name = "test"
        faker = Faker()
        s3_key = f"{faker.file_path(depth=3, category='image')}"
        await create_bucket_file(bucket_name, s3_key)

    asyncio.run(main())
