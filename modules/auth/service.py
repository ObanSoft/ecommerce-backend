from sqlalchemy.ext.asyncio import AsyncSession
from modules.auth.security import hash_password, verify_password
from modules.users.repository import UserRepository
from common.enums import UserRole
from fastapi import HTTPException, status
from modules.users.model import User
from modules.auth.validators import validate_password

class AuthService:  # Agrupa la logica de registro y autenticación

    @staticmethod  # Es una función que pertenece a una clase pero no a una instancia 
    async def register(
        db: AsyncSession,
        username: str,
        email: str,
        password: str,
    ) -> User:
        try:
            validate_password(password)
        except ValueError as e:
            raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
        
        user_repo = UserRepository(db)

        user = await user_repo.get_by_email(email)

        if user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"  # Validación para no duplicar emails
            )
        
        hashed_password = hash_password(password)  # Función de hash
        
        return await user_repo.create(
            username=username,
            email=email,
            password_hash=hashed_password,
            role=UserRole.CLIENTE
        )
    
    @staticmethod
    async def authenticate(
        db: AsyncSession,
        email: str,
        password: str
    ) -> User:

        user_repo = UserRepository(db)

        user = await user_repo.get_by_email(email)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials"
            )

        if not verify_password(password, user.password_hash):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials"
            )

        if not user.is_active:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Inactive user"
            )

        return user

