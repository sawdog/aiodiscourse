import asyncio

from common import get_discourse_client

async def main():
    async with get_discourse_client() as client:
        results = await client.topics.reply(211, raw="This is a reply to this "
                                                    "topic.")
        print(f"Topic reply success:\n {results}")


asyncio.run(main())
