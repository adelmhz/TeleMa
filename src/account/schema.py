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
    password: Optional[str]

    class Config:
        orm_mode = True

class SendLoginCodeSchema(BaseModel):
    login_code: str

class LoginCodeSchema(BaseModel):
    code: str

class UserSimpleSchema(BaseModel):
    phone: Optional[str]
    username: Optional[str]

    class Config:
        orm_mode = True

class SuccessSchema(BaseModel):
    success: bool

class MessageSchema(BaseModel):
    from_user: UserSimpleSchema
    to_user: UserSimpleSchema
    date: Optional[datetime]
    text: Optional[str]

class SendMessageSchema(BaseModel):
    from_user: str
    to_user: str
    text: str