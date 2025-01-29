from sqlalchemy.orm import Session
from app.models.example import ExampleModel
from pydantic import BaseModel

# Схема для создания примера
class ExampleCreate(BaseModel):
    name: str
    description: str

# Схема для обновления примера
class ExampleUpdate(BaseModel):
    name: str
    description: str

# Схема для ответа с примером
class ExampleResponse(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        from_attributes = True

# Функция для создания нового примера
async def create_example(db: Session, example: ExampleCreate):
    db_example = ExampleModel(name=example.name, description=example.description)
    db.add(db_example)
    db.commit()
    db.refresh(db_example)
    return db_example

# Функция для получения примера по ID
async def get_example(db: Session, example_id: int):
    return db.query(ExampleModel).filter(ExampleModel.id == example_id).first()

# Функция для обновления примера по ID
async def update_example(db: Session, example_id: int, example: ExampleUpdate):
    db_example = db.query(ExampleModel).filter(ExampleModel.id == example_id).first()
    if db_example:
        db_example.name = example.name
        db_example.description = example.description
        db.commit()
        db.refresh(db_example)
    return db_example

# Функция для удаления примера по ID
async def delete_example(db: Session, example_id: int):
    db_example = db.query(ExampleModel).filter(ExampleModel.id == example_id).first()
    if db_example:
        db.delete(db_example)
        db.commit()
    return db_example