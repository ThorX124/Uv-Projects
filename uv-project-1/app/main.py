from fastapi import FastAPI
from app.api.todos import router as todo_router

app = FastAPI(
    title="Todo API",
    description="A simple API for managing todo items",
    version="1.0.0"
)


app.include_router(todo_router, prefix="/api")