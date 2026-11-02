from fastapi import FastAPI

app = FastAPI(
    title="Практическая работа №3",
    description="Первое приложение на FastAPI",
    version="1.0.0",
)


@app.get("/")
async def welcome() -> dict:
    return {"message": "Артем Черников"}
