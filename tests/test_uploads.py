import pytest
from aiodiscourse import AsyncDiscourseClient


@pytest.mark.asyncio
async def test_uploads(monkeypatch):
    async with AsyncDiscourseClient('http://demo', 'KEY', 'admin') as c:
        monkeypatch.setattr(c, 'get', lambda *a, **k: {'ok': True})
        ns = c.uploads;
        assert hasattr(ns, '__init__')
