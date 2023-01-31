from asyncio import sleep
from typing import Union
from sqlalchemy.orm.session import Session
from pyrogram import Client
from pyrogram.types import TermsOfService

from .schema import AddAccountBaseSchema
from core.config import settings
from core.models import Account
from db.database import session_local

async def add_account_task(db: Session, account: AddAccountBaseSchema):

    client = Client(
        account.phone,
        settings.API_ID,
        settings.API_HASH,
        password=account.password,
        in_memory=True
    )
    await client.connect()
    # Send Code
    send_code = await client.send_code(account.phone)
    # send_code = None
    login_code: Union[str, None] = None

    time_left = 0
    while not login_code:
        if time_left > 120:
            print('time is over.')
            return

        with session_local() as new_session:
            await sleep(2)
            account_obj: Account = new_session.query(Account).filter(
                Account.phone == account.phone).first()
            print("Waiting for login code ---------------=-=-=", account_obj.phone)
            print("Login Code is ================ ", account_obj.login_code)
            login_code = account_obj.login_code
            print("login_code var ================ ", login_code)
            print("while result: =================", not login_code)
            time_left += 2

    print("huuuuuuuuray")
    # Signing to account
    response = await client.sign_in(
        phone_number=account.phone,
        phone_code_hash=send_code.phone_code_hash,
        phone_code=login_code
    )
    # Check if accounts needs to be registered
    if isinstance(response, TermsOfService):
        await client.accept_terms_of_service(response.id)

    # save session string
    session_string = await client.export_session_string()
    print(session_string)
    account_obj = db.query(Account).filter(Account.phone == account.phone)
    account_obj.update({Account.login_code: None, Account.session: session_string})
    db.commit()

    # disconnect connection
    await client.disconnect()
