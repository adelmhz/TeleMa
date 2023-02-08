from sqlalchemy.orm.session import Session
from sqlalchemy.sql import func
from pyrogram import Client
from pyrogram.errors.exceptions.bad_request_400 import PeerFlood, ChannelInvalid

from core.config import settings
from core.models import Account, Member, Message, User, Report


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

async def add_to_group_task(chat_id: int, user: User, db: Session):
    members = [member.username for member in db.query(Member).all()]

    for member in members:
        member_added = False
        while not member_added:
            account = (db.query(Account)
                .filter(Account.user_id==user.id)
                .order_by(func.random())
                .first())

            async with Client(
                account.phone,
                settings.API_ID,
                settings.API_HASH,
                proxy=settings.PROXY,
                session_string=account.session) as app:
                    try:
                        await app.add_chat_members(chat_id=chat_id, user_ids=member)
                        Report.create_report(
                            db=db,
                            account_id=account.id,
                            action='add_to_group'
                        )
                        member_added = True
                    except PeerFlood:
                        print(f'{account.phone} is limited.============')
                    except ChannelInvalid:
                        print(f'{account.phone} is not an admin.-=-=-=-=-=-=-')
