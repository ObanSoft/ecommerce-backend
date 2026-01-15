from pydantic import BaseModel, EmailStr
from uuid import UUID
from common.enums import UserRole
from datetime import datetime

class UserResponse(BaseModel):
    id : UUID
    username: str
    email: EmailStr
    role : UserRole
    created_at : datetime

    class Config:
        from_attributes = True
        orm_mode = True
