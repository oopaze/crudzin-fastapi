from sqlalchemy import Column, String, Integer
from sqlalchemy_utils import EmailType

from app import pwd_context
from app.db import Base as Model

class User(Model):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    username = Column(String, unique=True)
    password = Column(String)
    email = Column(EmailType, unique=True)

    def __init__(self, name:str, username:str, password:str, email:str):
        self.name = name
        self.username = username
        self.password = self.generate_password(password) 
        self.email = email

    def generate_password(password):
        return pwd_context.hash(password)

    def __repr__(self) -> str:
        return f"< User - {self.name} >"
