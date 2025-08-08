import asyncio

from common import get_discourse_client


async def main():
    async with get_discourse_client() as client:
        results = await client.posts.reply(
            topic_id=211,
            post_id=234,
            raw="This is a reply to a post"
        )
        print(f"Post Reply success:\n {results}")


if __name__ == "__main__":
    asyncio.run(main())



asyncio.run(main())
