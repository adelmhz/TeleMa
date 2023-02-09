"""
Automate join clients to target group
"""
from pyrogram import Client

from core.models import Account
from core.config import settings
from db.database import session_local

with session_local() as db:
    all_accounts = Account.get_all_accounts(db=db)

    for account in all_accounts:
        with Client(
            account.phone,
            settings.API_ID,
            settings.API_HASH,
            proxy=settings.PROXY,
            session_string=account.session) as app:
                app.join_chat('iarba_dulce_vip')