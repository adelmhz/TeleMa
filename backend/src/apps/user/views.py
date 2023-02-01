from fastapi import APIRouter, Depends

from core.deps import get_user_by_header
from core.models import User

router = APIRouter(
    prefix='/users',
    tags=['users']
)

@router.get('/me/status')
def get_user_status(user: User=Depends(get_user_by_header)):
    return {'is_active': user.is_active}