import asyncio

from common import get_discourse_client


async def main():
    async with get_discourse_client() as client:
        async for topic in client.topics.iter_latest():
            print(topic["title"])

asyncio.run(main())
