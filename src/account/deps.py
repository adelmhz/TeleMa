from typing import AsyncGenerator, Optional
from pyrogram import Client
from pyrogram.types import Message
from core.config import settings


async def get_client() -> AsyncGenerator:
    client = Client(
            settings.phone,
            api_id=settings.API_ID,
            api_hash=settings.API_HASH,
            session_string=settings.session_string
    )
    try:
        await client.connect()
        yield client
    finally:
        await client.disconnect()

async def new_client():
    client = Client(
            ':on-memory',
            api_id=settings.API_ID,
            api_hash=settings.API_HASH,
            in_memory=True
    )
    try:
        await client.connect()
        yield client
    finally:
        await client.disconnect()

