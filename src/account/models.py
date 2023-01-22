import datetime
from sqlalchemy import (
    Column, ForeignKey, Integer, String, Boolean, DateTime
)
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types.choice import ChoiceType

from db.database import Base

class Account(Base):
    STATUSES = [
        ('active', 'Active'),
        ('ban', 'Ban')
    ]

    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True, index=True)
    phone = Column(String, nullable=True)
    session = Column(String, nullable=True)
    ip = Column(String, nullable=True)
    status = Column(ChoiceType(STATUSES))
    action_time = Column(DateTime, default=datetime.datetime.utcnow)

class Member(Base):
    STATUSES = [
        ('added', 'Added'),
        ('send', 'Send')
    ]

    __tablename__ = 'members'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=True)
    status = Column(ChoiceType(STATUSES), nullable=True)
    action_time = Column(DateTime, default=datetime.datetime.utcnow)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    chat_id = Column(String, nullable=True)
    package = Column(String, nullable=True)


