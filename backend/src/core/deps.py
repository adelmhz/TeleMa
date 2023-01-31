from typing import AsyncGenerator
from fastapi import Depends
from pyrogram import Client
from pyrogram.types import Message
from sqlalchemy.orm.session import Session

from core.config import settings
from core.models import User
from db.database import get_db


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


async def get_user(db: Session=Depends(get_db)) -> User:
    user = db.query(User).filter(User.id==1).first()
    return user
