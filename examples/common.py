import os
from aiodiscourse import AsyncDiscourseClient

try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass


def get_required_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


def get_discourse_client() -> AsyncDiscourseClient:
    return AsyncDiscourseClient(
        base_url=os.getenv("DISCOURSE_URL", "https://localhost:3000"),
        api_key=get_required_env("DISCOURSE_APIKEY"),
        api_username=os.getenv("DISCOURSE_API_USERNAME", "admin"),
    )
