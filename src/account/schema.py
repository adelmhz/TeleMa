from typing import Optional
from datetime import datetime
from pydantic import BaseModel

class AccountSimpleSchema(BaseModel):
    id: int
    phone: str
    status: str

    class Config:
        orm_mode = True

class AddAccountBaseSchema(BaseModel):
    phone: str
    code: str
    phone_code_hash: str
    password: Optional[str]

    class Config:
        orm_mode = True

class PhoneCodeHashSchema(BaseModel):
    phone_code_hash: str

class UserSimpleSchema(BaseModel):
    phone: Optional[str]
    username: Optional[str]

class MessageSchema(BaseModel):
    from_user: UserSimpleSchema
    to_user: UserSimpleSchema
    date: Optional[datetime]
    text: Optional[str]
