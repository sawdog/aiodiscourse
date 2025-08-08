import asyncio

from common import get_discourse_client


async def main():
    async with get_discourse_client() as client:
        for i in range(5):
            topic = await client.topics.create(
                title=f'Batch Topic {i + 1}',
                raw=f'This is the content for topic {i + 1}.',
            )
            print(f"Created topic {topic.get('topic_id') or topic.get('id')}")


asyncio.run(main())
