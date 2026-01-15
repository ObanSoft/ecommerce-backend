from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession # Crea motor de conexion y abre sesiones a la db
from sqlalchemy.orm import sessionmaker, DeclarativeBase # Define como crear las sesiones
from core.config import settings # Conexion a la config de la db (Infra)

engine = create_async_engine( # Administrador de conexiones 
    settings.DATABASE_URL,
    echo = True
)

AsyncSessionLocal = sessionmaker( 
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

class Base(DeclarativeBase): # Registra todos los modelos y mantiene el metadata
    pass

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

import models