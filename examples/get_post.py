import asyncio
import os

from aiodiscourse import AsyncDiscourseClient

API_KEY = os.environ.get("DISCOURSE_APIKEY")
URL = os.getenv("DISCOURSE_URL",
                          "https://localhost:3000")
USERNAME = os.getenv("DISCOURSE_API_USERNAME", "admin")


async def main():
    async with AsyncDiscourseClient(
        base_url=URL,
        api_key=API_KEY,
        api_username=USERNAME,
    ) as client:
        results = await client.posts.get(234)
        print(f"Post fetched successfully.\n {results}")


asyncio.run(main())
