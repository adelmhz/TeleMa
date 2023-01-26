import os
from typing import List
from fastapi import APIRouter, Depends, HTTPException, UploadFile, status
from sqlalchemy.orm.session import Session
from pyrogram import Client
from pyrogram.enums import ChatType


from core.config import settings
from db.database import get_db
from .deps import get_client, new_client
from .models import Account
from .schema import AccountSimpleSchema, LoginCodeSchema, MessageSchema, PhoneCodeHashSchema, AddAccountBaseSchema, SendMessageSchema, SuccessSchema, UserSimpleSchema

router = APIRouter(
    prefix='/accounts',
    tags=['account']
)


@router.get('/', response_model=List[AccountSimpleSchema])
async def get_all_accounts(db: Session = Depends(get_db)):
    """
    Get all accounts of user's telegram bots.
    """
    return await Account.get_all_accounts(db)


@router.get('/{phone}', response_model=AccountSimpleSchema)
async def get_account(phone: str, db: Session = Depends(get_db)):
    """
    Get account of user's telegram bot.
    """
    return await Account.get_account_by_phone(db, phone)


@router.post('/sent_code/{phone}', response_model=PhoneCodeHashSchema)
async def sent_code(
    phone: str,
    client=Depends(new_client)
):
    """
    Send telegram code and return phone hash code of account.
    """
    code = await client.send_code(phone)
    return {'phone_code_hash': code.phone_code_hash}


@router.get('/{account}/login-code')
async def get_login_code(
    account: str,
    client: Client = Depends(get_client)
):
    """
    Get last message of telegram chat and return login code.
    """
    last_message = client.get_chat_history(
        chat_id=settings.TELEGRAM_CHAT_ID, limit=1)
    async for message in last_message:
        return LoginCodeSchema(code=message.text)


@router.post('/{phone}', response_model=AccountSimpleSchema)
async def add_account(
    account: AddAccountBaseSchema,
    client=Depends(get_client),
    db: Session = Depends(get_db)
):
    """
    Add telegram account for user.
    """

    user = await client.sign_in(
        phone=account.phone,
        phone_code_hash=account.phone_code_hash,
        code=account.code,
        password=account.password
    )
    session_string = await client.session.save()
    print(session_string)
    account_obj = Account(phone=user.phone, session=session_string)
    db.add(account)
    db.commit()
    db.refresh(account_obj)
    return account_obj


@router.post('/{account}/profile/photo', response_model=SuccessSchema)
def change_profile_photo(
    account: str,
    photo: UploadFile,
    client: Client = Depends(get_client)
):
    """
    Change profile photo of an account.
    """
    if photo.content_type != 'image/jpeg':
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail='send valid image.')

    file_path = os.path.join(settings.UPLOAD_PATH, f'{account}-{photo.filename}')
    try:
        contents = photo.file.read()
        with open(file_path, 'wb') as f:
            f.write(contents)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='There was an error uploading a file.'
        )
    finally:
        photo.file.close()

    client.me = client.get_me()
    uploaded = client.set_profile_photo(photo=file_path)
    os.remove(file_path)

    if uploaded:
        return SuccessSchema(success=True)
    else:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='Something went wrongs.'
        )


@router.get('/{account}/messages/unreads', response_model=List[MessageSchema], tags=['messages'])
def get_unread_messages(account: str, client: Client = Depends(get_client)):
    """
    Get all unread messages of accounts and return messages.
    """
    result = []
    for dialog in client.get_dialogs():
        if dialog.chat.type == ChatType.PRIVATE and \
                dialog.unread_messages_count:
            last_message = dialog.top_message
            unread_messages = client.get_chat_history(
                dialog.chat.id, offset_id=last_message.id+1,
                limit=dialog.unread_messages_count
            )
            for message in unread_messages:
                from_user = UserSimpleSchema(
                    phone=message.from_user.phone_number,
                    username=message.from_user.username
                )
                to_user = UserSimpleSchema(phone=client.get_me().phone_number)
                result.append(
                    MessageSchema(
                        from_user=from_user,
                        to_user=to_user,
                        date=message.date,
                        text=message.text
                    )
                )
            client.read_chat_history(chat_id=dialog.chat.id)

    return result


@router.post(
    '/{account}/messages/send',
    response_model=MessageSchema,
    tags=['messages']
)
def send_message(
    account: str,
    request: SendMessageSchema,
    client: Client = Depends(get_client)
):
    me = client.get_me()

    message = client.send_message(chat_id=request.to_user, text=request.text)
    return MessageSchema(
        from_user=UserSimpleSchema(phone=me.phone_number),
        to_user=UserSimpleSchema(username=message.chat.username),
        date=message.date,
        text=message.text
    )
