from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.crud.example import create_example, get_example, update_example, delete_example
from app.schemas.example import ExampleCreate, ExampleUpdate, ExampleResponse
from app.db.session import get_db

# Создаем маршрутизатор для эндпоинтов
router = APIRouter()

# Эндпоинт для создания нового примера
@router.post("/", response_model=ExampleResponse)
async def create_example_endpoint(example: ExampleCreate, db: Session = Depends(get_db)):
    db_example = await create_example(db, example)
    return db_example

# Эндпоинт для получения примера по ID
@router.get("/{example_id}", response_model=ExampleResponse)
async def read_example(example_id: int, db: Session = Depends(get_db)):
    db_example = await get_example(db, example_id)
    if db_example is None:
        raise HTTPException(status_code=404, detail="Example not found")
    return db_example

# Эндпоинт для обновления примера по ID
@router.put("/{example_id}", response_model=ExampleResponse)
async def update_example_endpoint(example_id: int, example: ExampleUpdate, db: Session = Depends(get_db)):
    db_example = await update_example(db, example_id, example)
    if db_example is None:
        raise HTTPException(status_code=404, detail="Example not found")
    return db_example

# Эндпоинт для удаления примера по ID
@router.delete("/{example_id}", response_model=ExampleResponse)
async def delete_example_endpoint(example_id: int, db: Session = Depends(get_db)):
    db_example = await delete_example(db, example_id)
    if db_example is None:
        raise HTTPException(status_code=404, detail="Example not found")
    return db_example