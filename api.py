from fastapi import FastAPI

from todo import todo_router


app = FastAPI(
    title="Практическая работа №4",
    description="CRUD-приложение для управления задачами.",
    version="1.0.0"
)

app.include_router(todo_router, tags=["Задачи"])


@app.get("/")
async def root() -> dict:
    return {
        "message": "Приложение FastAPI запущено."
    }
