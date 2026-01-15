from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Ecommerce API"
    
    DB_HOST : str
    DB_PORT : int
    DB_NAME : str
    DB_USER :str
    DB_PASSWORD :str

    JWT_SECRET_KEY: str = "AW7813728SA1KSLAK12"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    @property # Convertimos la funcion en solo lectura
    def DATABASE_URL(self) -> str:
        return (
            f"postgresql+asyncpg://{self.DB_USER}:"
            f"{self.DB_PASSWORD}@{self.DB_HOST}:"
            f"{self.DB_PORT}/{self.DB_NAME}"
        )
    
    class Config:
        env_file = ".env" # Metadata para cargar variables 

settings = Settings()

