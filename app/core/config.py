from pydantic import BaseSettings
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    app_name: str = "My FastAPI Application"
    admin_email: str = "admin@example.com"
    items_per_page: int = 50

    class Config:
        env_file = ".env"

settings = Settings()

# Создаем базовый класс для моделей
Base = declarative_base()

# Определяем модель ExampleModel
class ExampleModel(Base):
    __tablename__ = 'example'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)