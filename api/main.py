from fastapi import FastAPI
from .routers import users
from db import SessionLocal

app = FastAPI()
app.include_router(users.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
