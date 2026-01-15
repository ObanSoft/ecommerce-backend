from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional
from sqlalchemy import select
from modules.users.model import User

class UserRepository: # Nos ayuda a interacturar con la sql y no meter el service

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_email(self, email: str) -> Optional[User]:
        result = await self.db.execute(
            select(User).where(User.email == email)
        )
        return result.scalar_one_or_none()

    async def create( 
        self,
        email: str,
        password_hash: str,
        role
    ) -> User:
        user = User(
            email=email,
            password_hash=password_hash,
            role=role
        )
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user
