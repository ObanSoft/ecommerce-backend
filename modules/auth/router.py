from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import get_db
from modules.auth.schemas import RegisterRequest, LoginRequest, TokenResponse
from modules.auth.service import AuthService
from modules.auth.jwt import create_access_token

router = APIRouter(prefix='/auth', tags=["Auth"])

@router.post("/register")
async def register(
    data: RegisterRequest,
    db: AsyncSession = Depends(get_db)
):

    user = await AuthService.register(
        db=db,
        email=data.email,
        password=data.password
    )

    return {"message" : "User registered succesfully"}

@router.post("/login", response_model=TokenResponse)
async def login(
    data: LoginRequest,
    db: AsyncSession = Depends(get_db)
):
    user = await AuthService.authenticate(
        db=db,
        email=data.email,
        password=data.password
    )

    token = create_access_token({
        "sub": str(user.id),
        "role": user.role.value
    })

    return TokenResponse(
        access_token=token,
        role = user.role.value
    )