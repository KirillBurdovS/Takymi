from fastapi import APIRouter, HTTPException
from app.crud.example import create_example, get_example, update_example, delete_example
from app.schemas.example import ExampleCreate, ExampleUpdate, ExampleResponse

# Создаем маршрутизатор для эндпоинтов
router = APIRouter()

# Эндпоинт для создания нового примера
@router.post("/", response_model=ExampleResponse)
async def create_example_endpoint(example: ExampleCreate):
    db_example = await create_example(example)
    return db_example

# Эндпоинт для получения примера по ID
@router.get("/{example_id}", response_model=ExampleResponse)
async def read_example(example_id: int):
    db_example = await get_example(example_id)
    if db_example is None:
        raise HTTPException(status_code=404, detail="Example not found")
    return db_example

# Эндпоинт для обновления примера по ID
@router.put("/{example_id}", response_model=ExampleResponse)
async def update_example_endpoint(example_id: int, example: ExampleUpdate):
    db_example = await update_example(example_id, example)
    if db_example is None:
        raise HTTPException(status_code=404, detail="Example not found")
    return db_example

# Эндпоинт для удаления примера по ID
@router.delete("/{example_id}", response_model=ExampleResponse)
async def delete_example_endpoint(example_id: int):
    db_example = await delete_example(example_id)
    if db_example is None:
        raise HTTPException(status_code=404, detail="Example not found")
    return db_example