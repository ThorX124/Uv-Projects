from fastapi import FastAPI

app = FastAPI(
    title="Todo API",
    description="A simple API for managing todo items",
    version="1.0.0"
)


app.include_router(todo_router, prefix="/api")