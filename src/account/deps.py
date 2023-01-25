from typing import Optional
from pyrogram import Client
from pyrogram.types import Message
from core.config import settings


async def get_client() -> Optional[Client]:
    client = Client(
        settings.phone,
        api_id=settings.API_ID,
        api_hash=settings.API_HASH,
        session_string=settings.session_string
    )
    await client.connect()
    return client

