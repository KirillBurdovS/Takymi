from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Создаем базу данных SQLite
# Здесь указывается URL для подключения к базе данных SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# Создаем движок базы данных
# Движок используется для связи с базой данных
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Создаем сессию для работы с базой данных
# SessionLocal будет использоваться для создания новых сессий
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Создаем базовый класс для моделей
# Все модели будут наследоваться от этого базового класса
Base = declarative_base()

# Функция для получения сессии базы данных
# Эта функция будет использоваться для получения сессии в каждом запросе
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()