from fastapi import FastAPI

app = FastAPI(
    title="Ecommerce API",
    version="1.0.0"
)

@app.get("/check")
async def check():
    return {"Status" : "OK"}