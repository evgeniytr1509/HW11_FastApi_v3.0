from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ..database.models import Contact  


SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Определение Base
Base = declarative_base()

# создание базі данных
Base.metadata.create_all(bind=engine)

# Функция для получения сессии базы данных
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# модель Contact для работы с контактами

def create_contact(first_name: str, last_name: str, email: str, phone_number: str, birthday: Date, additional_data: str = None):
    contact = Contact(
        first_name=first_name,
        last_name=last_name,
        email=email,
        phone_number=phone_number,
        birthday=birthday,
        additional_data=additional_data
    )
    db = SessionLocal()
    try:
        db.add(contact)
        db.commit()
        db.refresh(contact)
        return contact
    finally:
        db.close()