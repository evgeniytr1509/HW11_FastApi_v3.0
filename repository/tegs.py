from sqlalchemy.orm import Session
from database.models import Tag
from schemas import TagCreate

class TagRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_tag(self, tag_id: int):
        return self.db.query(Tag).filter(Tag.id == tag_id).first()

    def get_all_tags(self, skip: int = 0, limit: int = 10):
        return self.db.query(Tag).offset(skip).limit(limit).all()

    def create_tag(self, tag: TagCreate):
        db_tag = Tag(**tag.dict())
        self.db.add(db_tag)
        self.db.commit()
        self.db.refresh(db_tag)
        return db_tag

    def update_tag(self, tag_id: int, tag_data: TagCreate):
        db_tag = self.get_tag(tag_id)
        for key, value in tag_data.dict(exclude_unset=True).items():
            setattr(db_tag, key, value)
        self.db.commit()
        self.db.refresh(db_tag)
        return db_tag

    def delete_tag(self, tag_id: int):
        db_tag = self.get_tag(tag_id)
        self.db.delete(db_tag)
        self.db.commit()
        return db_tag