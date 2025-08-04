import pytest
from aiodiscourse import AsyncDiscourseClient
import asyncio


@pytest.mark.asyncio
async def test_topics_list(discourse_url, api_key, api_user):
    async with AsyncDiscourseClient(discourse_url, api_key, api_user) as client:
        latest = await client.topics.list_latest()
        assert 'topic_list' in latest
