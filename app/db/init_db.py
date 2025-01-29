from app.db.session import engine, Base
from app.models.team import TeamLead, Participant
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.crud.example import create_example, get_example, update_example, delete_example
from app.schemas.example import ExampleCreate, ExampleUpdate, ExampleResponse
from app.db.session import get_db
import logging

Base.metadata.create_all(bind=engine)

# Создаем маршрутизатор для эндпоинтов
router = APIRouter()

# Настраиваем логирование
logger = logging.getLogger(__name__)

# Эндпоинт для создания нового примера
@router.post("/", response_model=ExampleResponse)
async def create_example_endpoint(example: ExampleCreate, db: Session = Depends(get_db)):
    try:
        db_example = await create_example(db, example)
        logger.info(f"Example created with ID: {db_example.id}")
        return db_example
    except Exception as e:
        logger.error(f"Error creating example: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Эндпоинт для получения примера по ID
@router.get("/{example_id}", response_model=ExampleResponse)
async def read_example(example_id: int, db: Session = Depends(get_db)):
    try:
        db_example = await get_example(db, example_id)
        if db_example is None:
            logger.warning(f"Example with ID {example_id} not found")
            raise HTTPException(status_code=404, detail="Example not found")
        return db_example
    except Exception as e:
        logger.error(f"Error reading example: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Эндпоинт для обновления примера по ID
@router.put("/{example_id}", response_model=ExampleResponse)
async def update_example_endpoint(example_id: int, example: ExampleUpdate, db: Session = Depends(get_db)):
    try:
        db_example = await update_example(db, example_id, example)
        if db_example is None:
            logger.warning(f"Example with ID {example_id} not found")
            raise HTTPException(status_code=404, detail="Example not found")
        logger.info(f"Example with ID {example_id} updated")
        return db_example
    except Exception as e:
        logger.error(f"Error updating example: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Эндпоинт для удаления примера по ID
@router.delete("/{example_id}", response_model=ExampleResponse)
async def delete_example_endpoint(example_id: int, db: Session = Depends(get_db)):
    try:
        db_example = await delete_example(db, example_id)
        if db_example is None:
            logger.warning(f"Example with ID {example_id} not found")
            raise HTTPException(status_code=404, detail="Example not found")
        logger.info(f"Example with ID {example_id} deleted")
        return db_example
    except Exception as e:
        logger.error(f"Error deleting example: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")