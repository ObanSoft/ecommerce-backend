
from modules.users.schemas import UserResponse
from common.dependencies.get_current_admin_user import get_current_admin_user
from modules.users.model import User
from fastapi import APIRouter, Depends, HTTPException, status
from modules.users.service import UserService
from common.dependencies.auth import get_current_user
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import get_db

router =APIRouter(prefix="/api/v1", tags=["Admins"])

@router.get("/users", response_model=list[UserResponse])
async def get_all_users(
    admin_user: User = Depends(get_current_admin_user),
    service: UserService = Depends()
):
    return await service.get_all_users()

@router.get("/admin/users/{username}", response_model=UserResponse)
async def get_user_by_username_admin(
    username: str,
    admin_user: User = Depends(get_current_admin_user),
    service: UserService = Depends()
):
    user = await service.get_by_username(username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user