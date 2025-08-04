import click
import asyncio
import os

from aiodiscourse import AsyncDiscourseClient


@click.group()
def cli():
    """CLI for interacting with the aiodiscourse module."""
    pass

def get_client():
    return AsyncDiscourseClient(
        base_url=os.environ.get("DISCOURSE_URL"),
        api_key=os.environ.get("DISCOURSE_APIKEY"),
        api_username=os.environ.get("DISCOURSE_API_USERNAME"),
    )

@cli.command()
@click.argument("topic_id", type=int)
def get_topic(topic_id):
    """Fetch and display a topic by ID."""
    client = get_client()

    async def _get():
        topic = await client.topics.get(topic_id)
        click.echo(topic)

    asyncio.run(_get())
