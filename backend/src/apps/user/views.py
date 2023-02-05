from fastapi import APIRouter, Depends, Response
from requests import Session

from core.deps import get_user_by_header
from core.models import User
from db.database import get_db
from .schema import UserStatusSchema

router = APIRouter(
    prefix='/users',
    tags=['users']
)

@router.get('/me/status')
async def get_user_status(
    user: User=Depends(get_user_by_header)
):
    return Response(content={'is_active': user.is_active})

@router.get('/me/status/step', response_model=UserStatusSchema)
async def get_user_status_step(
    db: Session=Depends(get_db),
    user: User=Depends(get_user_by_header)
):
    have_accounts = await User.have_accounts(db, user)
    have_members = await User.have_members(db, user)

    return UserStatusSchema(
        have_accounts=have_accounts,
        have_members=have_members,
        is_active=user.is_active
    )

