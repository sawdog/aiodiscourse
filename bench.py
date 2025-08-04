import asyncio
import argparse
import time

from aiodiscourse import AsyncDiscourseClient


async def sequential_fetch(client, pages):
    count = 0
    async for topic in client.topics.iter_latest(
            max_pages=pages, concurrency=1,
    ):
        count += 1
    return count


async def parallel_fetch(client, pages):
    count = 0
    async for topic in client.topics.iter_latest(
            max_pages=pages, concurrency=5,
    ):
        count += 1
    return count


async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--base-url', required=True)
    parser.add_argument('--api-key', required=True)
    parser.add_argument('--api-user', required=True)
    parser.add_argument('--pages', type=int, default=5)
    args = parser.parse_args()
    async with AsyncDiscourseClient(
            args.base_url, args.api_key, args.api_user,
    ) as client:
        start = time.time()
        seq = await sequential_fetch(client, args.pages)
        seq_time = time.time() - start
        start = time.time()
        par = await parallel_fetch(client, args.pages)
        par_time = time.time() - start
        print(f"Sequential: {seq} topics in {seq_time:.2f}s")
        print(f"Parallel:   {par} topics in {par_time:.2f}s")


if __name__ == '__main__':
    asyncio.run(main())
