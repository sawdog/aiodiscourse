import asyncio

from common import get_discourse_client


async def main():
    async with get_discourse_client() as client:
        results = await client.posts.get(234)
        print(f"Post fetched successfully.\n {results}")


asyncio.run(main())
