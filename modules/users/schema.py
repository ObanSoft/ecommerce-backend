from pydantic import BaseModel, EmailStr
from uuid import UUID
from common.enums import UserRole

class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserRead(BaseModel):
    id: UUID
    email: EmailStr
    role: UserRole
    is_active : bool

    class Config:
        from_attributes = True