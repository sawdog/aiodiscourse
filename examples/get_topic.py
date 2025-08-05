import asyncio

from common import get_discourse_client

async def main():
    async with get_discourse_client() as client:
        results = await client.topics.get(211)
        print(f"Topic fetched successfully.\n {results}")


asyncio.run(main())
