from sqlalchemy.orm import Session
from ..database.models import Contact
from ..database.db import SessionLocal, database


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_contacts(db: Session):
    return db.query(Contact).all()

def get_contact_by_id(db: Session, contact_id: int):
    return db.query(Contact).filter(Contact.id == contact_id).first()

def create_contact(db: Session, contact_data):
    contact = Contact(**contact_data)
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact

def update_contact(db: Session, contact_id: int, contact_data):
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    for key, value in contact_data.items():
        setattr(contact, key, value)
    db.commit()
    db.refresh(contact)
    return contact

def delete_contact(db: Session, contact_id: int):
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    db.delete(contact)
    db.commit()
    return {"message": "Contact successfully deleted"}