# Quickstart Guide for aiodiscourse

This guide helps you quickly start using the `aiodiscourse` async client for 
the Discourse API.

---

## Set Environment Variables

Before using the client or CLI, configure the following three required 
values. You can set them in a `.env` file or directly in your environment:

### Required Variables

- `DISCOURSE_URL`: Base URL of your Discourse instance (e.g., 
  `https://discourse.example.com`)
- `DISCOURSE_APIKEY`: API key for an admin or system user
- `DISCOURSE_APIUSER`: Username associated with the API key

### `.env` file

Create a `.env` file:

```dotenv
DISCOURSE_URL=https://discourse.example.com
DISCOURSE_APIKEY=your-api-key
DISCOURSE_APIUSER=your-username
```

### Directly in Environment
```bash
export DISCOURSE_URL=https://discourse.example.com
export DISCOURSE_APIKEY=your-api-key
export DISCOURSE_APIUSER=your-username
```

## Run the CLI
```bash
discourse --help

Usage: discourse [OPTIONS] COMMAND [ARGS]...

  CLI for interacting with the aiodiscourse module.

Options:
  --url TEXT           Discourse base URL  [required]
  --api-key TEXT       Discourse API key  [required]
  --api-username TEXT  Discourse API username  [required]
  --help               Show this message and exit.

Commands:
  close-topic  Close a topic by its ID.
  get-topic    Fetch and display a topic by ID.
```

## Examples

You can run example scripts to see how to use the `aiodiscourse` client.

### Running an Example Script
There are several example scripts in the `examples/` directory.

```bash
python examples/get_topic.py
```

### Using in Code
```python
import asyncio
import os
from aiodiscourse import AsyncDiscourseClient

async def main():
    client = AsyncDiscourseClient(
        base_url=os.environ["DISCOURSE_URL"],
        api_key=os.environ["DISCOURSE_APIKEY"],
        api_username=os.environ["DISCOURSE_APIUSER"]
    )
    topics = await client.topics.list()
    for topic in topics["topic_list"]["topics"]:
        print(topic["title"])

asyncio.run(main())
```



