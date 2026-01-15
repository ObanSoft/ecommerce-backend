from pydantic import BaseModel, EmailStr


class RegisterRequest(BaseModel): # Input de registro
    username: str
    email : EmailStr
    password : str


class LoginRequest(BaseModel): # Input de login
    email : EmailStr
    password: str


class TokenResponse(BaseModel): # Output de login
    username: str
    access_token : str
    token_type : str = "bearer"
    role : str