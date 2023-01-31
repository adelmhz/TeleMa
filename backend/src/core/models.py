import datetime
from fastapi import HTTPException, status
from sqlalchemy import (
    Column, ForeignKey, Integer, String, DateTime, Text
)
from sqlalchemy.orm import relationship, Session

from db.database import Base
from apps.services.schema import CreateMessageSchema

class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True, index=True)
    phone = Column(String(256), nullable=True)
    session = Column(String(550), nullable=True)
    ip = Column(String(55), nullable=True)
    status = Column(String(55), nullable=True)
    action_time = Column(DateTime, default=datetime.datetime.utcnow)
    login_code = Column(String(55), nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='accounts')

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

    @staticmethod
    async def create_account(db: Session, user, request, status='active'):
        account = Account(
            phone=request.phone,
            status=status,
            user=user,
            user_id=user.id,
        )
        db.add(account)
        db.commit()
        db.refresh(account)
        return account

class Member(Base):
    __tablename__ = 'members'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(55), nullable=True)
    status = Column(String(55), nullable=True)
    action_time = Column(DateTime, default=datetime.datetime.utcnow)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    chat_id = Column(String(55), nullable=True)
    package = Column(String(55), nullable=True)
    messages = relationship(
        'Message', back_populates='user',
        cascade="all, delete", passive_deletes=True)
    accounts = relationship(
        'Account', back_populates='user'
    )


class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=True)
    # media = ...
    user_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"))
    user = relationship('User', back_populates='messages')

    @staticmethod
    async def get_all_messages(db: Session, user: User):
        return db.query(Message).filter(
            Message.user_id==user.id
        ).all()


    @staticmethod
    async def get_message(id: int, db: Session, user: User):
        message = db.query(Message).filter(
            Message.id==id,
            Message.user_id==user.id
        ).first()
        return message

    @staticmethod
    async def create_message(request: CreateMessageSchema, db: Session, user: User):
        new_message = Message(user_id=user.id, text=request.text)
        db.add(new_message)
        db.commit()
        db.refresh(new_message)
        return new_message

    @staticmethod
    async def delete_message(id: int, db: Session, user: User):
        message = db.query(Message).filter(
            Message.id==id,
            Message.user_id==user.id
        ).first()
        db.delete(message)
        db.commit()
        return 'ok'
