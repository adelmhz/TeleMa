from pydantic import BaseModel

class AddGroupSchema(BaseModel):
    chat_id: str

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