from app.db import session
from typing import List, Optional
from .models import User

db = session

def get_users() -> List[User]:
    """
        Take all users from database
    """
    return db.query(User).all()

def get_user(user_id: int) -> User:
    """
        Search an user by his id
    """
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_username(username: str) -> User:
    """
        Search an user by his username
    """
    return db.query(User).filter(User.username == username).first()
