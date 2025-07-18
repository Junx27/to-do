from fastapi import FastAPI
from app.core.database import engine
from app.core.database import Base
from app.models import *
from app.api.v1 import *

app = FastAPI()

# Manual migration: create tables if not exist
Base.metadata.create_all(bind=engine)

# Register router
app.include_router(todo.router, prefix="/api/v1")
app.include_router(status_todo.router, prefix="/api/v1")
app.include_router(category.router, prefix="/api/v1")
