import pytest
from aiodiscourse import AsyncDiscourseClient


@pytest.mark.asyncio
async def test_topics(monkeypatch):
    async with AsyncDiscourseClient('http://demo', 'KEY', 'admin') as c:
        monkeypatch.setattr(c, 'get', lambda *a, **k: {'ok': True})
        ns = c.topics;
        assert hasattr(ns, '__init__')
