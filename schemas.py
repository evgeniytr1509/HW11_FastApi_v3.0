from pydantic import BaseModel
from typing import Optional
from datetime import date

class ContactBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: str
    birthday: Optional[date] = None
    

class ContactCreate(ContactBase):
    pass

class ContactRead(ContactBase):
    id: int

    class Config:
        from_attributes = True
        