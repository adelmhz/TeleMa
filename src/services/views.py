from typing import List
from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException, status
from sqlalchemy.orm.session import Session

from .schema import AddGroupSchema, CreateMessageSchema, MessageSchema
from core.deps import get_user
from core.models import Message, User
from db.database import get_db
from .tasks import send_service_task

router = APIRouter(
    prefix='/services',
    tags=['services']
)


@router.get('/messages/all', response_model=List[MessageSchema])
async def get_all_messages(
    user: User = Depends(get_user),
    db: Session = Depends(get_db)
):
    """
    return all messages of user.
    """
    messages = await Message.get_all_messages(db, user)
    return messages


@router.get('/messages/{id}', response_model=MessageSchema)
async def get_message(
    id: int,
    user: User = Depends(get_user),
    db: Session = Depends(get_db)
):
    """
    return message of user by id.
    """
    return await Message.get_message(id, db, user)


@router.post('/messages', response_model=MessageSchema)
async def create_message(
    request: CreateMessageSchema,
    user: User = Depends(get_user),
    db: Session = Depends(get_db)
):
    """
    Create message for user.
    """
    return await Message.create_message(request, db, user)


@router.delete('/messages/{id}')
async def delete_message(
    id: int,
    user: User = Depends(get_user),
    db: Session = Depends(get_db)
):
    """
    Delete a message of user.
    """
    return await Message.delete_message(id, db, user)


@router.post('/send')
async def send_service(
    background_tasks: BackgroundTasks,
    user: User = Depends(get_user),
    db: Session=Depends(get_db)
):
    background_tasks.add_task(send_service_task, user, db)
    return {'message': 'started'}
