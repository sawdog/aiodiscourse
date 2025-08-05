import asyncio
import os
from dotenv import load_dotenv

from aiodiscourse import AsyncDiscourseClient

load_dotenv()

async def main():
    client = AsyncDiscourseClient(
        base_url=os.environ["DISCOURSE_URL"],
        api_key=os.environ["DISCOURSE_APIKEY"],
        api_username=os.environ["DISCOURSE_API_USERNAME"]
    )

    async for topic in client.topics.iter_latest():
        print(topic["title"])

asyncio.run(main())
