from fastapi import FastAPI
from modules.auth.router import router as auth_router
from modules.users.router import router as admins_user

app = FastAPI(
    title="Ecommerce API",
    version="1.0.0"
)

app.include_router(auth_router)
app.include_router(admins_user)
