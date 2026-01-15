import uuid
from sqlalchemy import String, Boolean, DateTime, Enum as SQLEnum 
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column # Tipado fuerte y definimos las columnas en la tabla
from sqlalchemy.sql import func # Usar funciones del motor sql

from core.database import Base #Infra de conexion a db
from common.enums import UserRole # Roles del usuario

class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    username: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False
    )

    email: Mapped[str] = mapped_column (
        String(255),
        unique=True,
        index=True, # Busquedas rapidas
        nullable=False 
    )

    password_hash: Mapped[str] = mapped_column (
        String(255),
        nullable=False
    )

    role : Mapped[UserRole] = mapped_column ( # Enumeración de python
        SQLEnum(UserRole, name="user_role"), 
        nullable=False,
        default=UserRole.CLIENTE
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at: Mapped[DateTime] = mapped_column(
    DateTime(timezone=True),
    server_default=func.now(),  
    onupdate=func.now()         
)