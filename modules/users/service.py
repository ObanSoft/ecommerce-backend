from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import get_db
from modules.admins.repository import AdminRepository
from modules.users.repository import UserRepository
from modules.users.model import User    
from typing import Optional

class UserService:
    def __init__(
        self,
        db: AsyncSession = Depends(get_db)
    ):
        self.repo = AdminRepository(db)  

    async def get_all_users(self):
        return await self.repo.get_all()

    async def get_by_username(self, username: str) -> Optional[User]:
        user = await self.repo.get_by_username(username)
        return user  
