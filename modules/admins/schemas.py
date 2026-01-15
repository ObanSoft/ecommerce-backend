from pydantic import BaseModel, EmailStr
from common.enums import UserRole

class AdminCreateUserRequest(BaseModel):
    email: EmailStr
    username: str
    password: str
    role: UserRole = UserRole.CLIENTE

class AdminUpdateUserRequest(BaseModel):
    email: EmailStr | None = None
    username: str | None = None
    role: UserRole | None = None
    is_active: bool | None = None