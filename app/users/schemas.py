from typing import Optional
from pydantic import BaseModel, EmailStr

class UserSchema(BaseModel):
    username: str
    password: str
    email: Optional[EmailStr]
    name: str

    class Config():
        orm_mode = True

class ReturnUserSchema(BaseModel):
    id: str
    username: str
    password: str
    email: Optional[EmailStr]
    name: str

    class Config:
        orm_mode = True
