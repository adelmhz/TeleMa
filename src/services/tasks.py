import random
from fastapi import Depends
from sqlalchemy.orm.session import Session
from sqlalchemy.sql import func
from pyrogram import Client

from core.config import settings
from core.models import Account, Member, Message, User
from db.database import get_db


async def send_service_task(user: User, db: Session):
    members = (
        db.query(Member)
        .order_by(func.random())
        .all())

    for member in members:
        account = (db.query(Account)
                .filter(Account.user_id==user.id)
                .order_by(func.random())
                .first())
        message = (
            db.query(Message)
            .filter(Message.user_id==user.id)
            .order_by(func.random())
            .first())

        async with Client(
        account.phone,
        settings.API_ID,
        settings.API_HASH,
        session_string=account.session) as app:
            await app.send_message(
                member.username, message.text
            )


