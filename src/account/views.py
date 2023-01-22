from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from db.database import get_db
from .models import Account
from .schema import AccountSchema

router = APIRouter(
    prefix='/accounts',
    tags=['account']
)

@router.get('/', response_model=List[AccountSchema])
def get_all_accounts(db: Session=Depends(get_db)):
    return Account.get_all_accounts(db)

@router.get('/{phone}', response_model=AccountSchema)
def get_account(phone: str, db: Session=Depends(get_db)):
    return Account.get_account_by_phone(db, phone)