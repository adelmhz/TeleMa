import datetime
from fastapi import HTTPException, status
from sqlalchemy import (
    Column, ForeignKey, Integer, String, Boolean, DateTime
)
from sqlalchemy.orm import relationship, Session
from sqlalchemy_utils.types.choice import ChoiceType

from db.database import Base

class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True, index=True)
    phone = Column(String, nullable=True)
    session = Column(String, nullable=True)
    ip = Column(String, nullable=True)
    status = Column(String, nullable=True)
    action_time = Column(DateTime, default=datetime.datetime.utcnow)

    @staticmethod
    async def get_all_accounts(db: Session):
        return db.query(Account).all()

    @staticmethod
    async def get_account_by_phone(db: Session, phone: str):
        account =  db.query(Account).filter(Account.phone==phone).first()
        if not account:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Account with phone {phone} not found!'
            )

        return account

class Member(Base):
    __tablename__ = 'members'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=True)
    status = Column(String, nullable=True)
    action_time = Column(DateTime, default=datetime.datetime.utcnow)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    chat_id = Column(String, nullable=True)
    package = Column(String, nullable=True)


