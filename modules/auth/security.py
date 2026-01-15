from passlib.context import CryptContext # Librería estándar para hashing de contraseñas

pwd_context = CryptContext( # Contexto de hashing 
    schemes=["bcrypt"],
    deprecated="auto"
)

def hash_password(password : str) -> str:
    return pwd_context.hash(password)

def verify_password(password: str, hashed_password: str) -> bool:
    return pwd_context.verify(password, hashed_password)




