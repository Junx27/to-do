from fastapi import FastAPI
from app.api.v1 import todo
from app.core.database import engine
from app.core.database import Base

app = FastAPI()

# Manual migration: create tables if not exist
Base.metadata.create_all(bind=engine)

# Register router
app.include_router(todo.router, prefix="/api/v1")
