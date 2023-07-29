from sqlalchemy.orm import Session
from ..database.models import Tag
from ..database.db import SessionLocal

def create_tag(db: Session, name: str):
    tag = Tag(name=name)
    db.add(tag)
    db.commit()
    db.refresh(tag)
    return tag

def get_tag(db: Session, tag_id: int):
    return db.query(Tag).filter(Tag.id == tag_id).first()

def get_tags(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Tag).offset(skip).limit(limit).all()

def update_tag(db: Session, tag_id: int, name: str):
    tag = db.query(Tag).filter(Tag.id == tag_id).first()
    if tag:
        tag.name = name
        db.commit()
        db.refresh(tag)
    return tag

def delete_tag(db: Session, tag_id: int):
    tag = db.query(Tag).filter(Tag.id == tag_id).first()
    if tag:
        db.delete(tag)
        db.commit()
    return tag