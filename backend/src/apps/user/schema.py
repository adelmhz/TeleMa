from pydantic import BaseModel

class UserStatusSchema(BaseModel):
    have_accounts: bool | None = None
    have_members: bool | None = None
    is_active: bool
