from fastapi import FastAPI
from app.api.v1.endpoints import team

# Создаем экземпляр FastAPI
app = FastAPI()

# Подключаем маршрутизатор для эндпоинтов из team
app.include_router(team.router, prefix="/api/v1", tags=["team"])

# Определяем корневой эндпоинт
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI backend!"}