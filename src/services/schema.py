from pydantic import BaseModel

class UserModelSimpleSchema(BaseModel):
    id: int
    chat_id: str

    class Config:
        orm_mode = True

class CreateMessageSchema(BaseModel):
    text: str

class MessageSchema(BaseModel):
    id: int
    text: str
    user: UserModelSimpleSchema

    class Config:
        orm_mode = True
