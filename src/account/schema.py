from pydantic import BaseModel

class AccountSchema(BaseModel):
    id: int
    phone: str
    status: str

    class Config:
        orm_mode = True
