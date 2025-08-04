import asyncio
import os

from aiodiscourse import AsyncDiscourseClient

API_KEY = os.environ.get("DISCOURSE_APIKEY")
URL = os.getenv("DISCOURSE_URL",
                          "https://localhost:3000")
USERNAME = os.getenv("DISCOURSE_API_USERNAME", "admin")


async def create_batch():
    async with AsyncDiscourseClient( base_url=URL,
                                     api_key=API_KEY,
                                     api_username=USERNAME,
                                     ) as client:
        for i in range(5):
            topic = await client.topics.create(
                title=f'Batch Topic {i + 1}',
                raw=f'This is the content for topic {i + 1}.',
            )
            print(f"Created topic {topic.get('topic_id') or topic.get('id')}")


asyncio.run(create_batch())
