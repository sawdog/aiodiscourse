from __future__ import annotations


class TopicsNamespace:
    def __init__(self, client):
        self.client = client

    async def create(self, title: str, raw: str, category_id: int = None,
                     **kwargs):
        payload = {"title": title, "raw": raw}
        if category_id:
            payload["category"] = category_id
        payload.update(kwargs)
        return await self.client.post("posts.json", json=payload)

    async def get(self, topic_id: int):
        return await self.client.get(f"t/{topic_id}.json")

    async def iter_latest(self, max_pages=None, concurrency=3):
        async for topic in self.client.iter_paginated(
                "latest.json", "topics", max_pages=max_pages,
                concurrency=concurrency,
        ):
            yield topic

    async def list_latest(self):
        return await self.client.get("latest.json")

    async def reply(self, topic_id: int, raw: str, reply_to_post_number: int | None = None):
        """
        Reply to a topic

        :param topic_id: ID of the topic to reply in
        :param raw: The content of the reply
        """
        payload = {
            "topic_id": topic_id,
            "raw": raw,
        }

        return await self.client.post("/posts", json=payload)


    # --- Undocumented/Admin Endpoints ---
    async def archive(self, topic_id: int):
        return await self.client.put(
            f"t/{topic_id}/status", json={"status": "archived"},
        )

    async def bump(self, topic_id: int):
        return await self.client.post(
            f"t/{topic_id}/timer", json={"status_type": "bump"},
        )
