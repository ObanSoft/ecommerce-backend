from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Ecommerce API"
    
    DB_HOST : str
    DB_PORT : int
    DB_NAME : str
    DB_USER :str
    DB_PASSWORD :str

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

