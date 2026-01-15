from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional
from sqlalchemy import select
from modules.users.model import User
from modules.users.repository import UserRepository
from typing import Optional
from sqlalchemy import select, func

class AdminRepository: # Nos ayuda a interacturar con la sql y no meter el service

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self):
        result = await self.db.execute(
            select(User)
        )
        return result.scalars().all()
    
    async def get_by_username(self, username: str) -> Optional[User]:
        result = await self.db.execute(
            select(User).where(func.lower(User.username) == username.lower())
        )
        return result.scalars().first()