from sqlalchemy import Column, Integer, String, Date, JSON
from database.db import Base
from ..routes.tags import Base  # Импорт Base из файла tags.py

class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, index=True)
    phone = Column(String, index=True)
    birthday = Column(Date)
    additional_data = Column(JSON, nullable=True)

class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)