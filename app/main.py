from fastapi import FastAPI
from app.routers import user, item
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Simple CRUD API Using FastAPI and SQLite Database")

app.include_router(user.router, prefix="/api/users", tags=["Users"])
app.include_router(item.router, prefix="/api", tags=["items"])