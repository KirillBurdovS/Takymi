from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Создаем базовый класс для моделей
Base = declarative_base()

# Определяем модель ExampleModel
class ExampleModel(Base):
    __tablename__ = 'example'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)