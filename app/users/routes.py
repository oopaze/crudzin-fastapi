from fastapi import APIRouter, HTTPException
from typing import List

from .schemas import UserSchema, ReturnUserSchema
from .crud import get_users, get_user
from app.db import session as db
from app import pwd_context
from .models import User

route = APIRouter()

@route.get("/{user_id}", response_model=ReturnUserSchema, response_model_exclude=['password'])
def read_user(user_id: int) -> ReturnUserSchema:
    """
        Show user of id passed omitting their password
    """
    user = get_user(user_id)
    return user

@route.get("/", response_model=List[ReturnUserSchema], response_model_exclude=['password'])
def read_users() -> List[ReturnUserSchema]:
    """
        Show all user in database omitting their password
    """
    users = get_users()
    return users

@route.post("/", response_model=UserSchema, response_model_exclude=['password'], status_code=201)
def create_user(user: UserSchema) -> User:
    """
        Add a new user based on UserSchema passed
    """
    new_user = User(**user.__dict__)

    db.add(new_user)
    db.commit()

    return user

@route.put("/{user_id}", response_model=UserSchema)
def update_user(user_id: int, user: UserSchema) -> UserSchema:
    """
        Update user selected by id and
        change him based on UserSchema passed
    """
    user_update = get_user(user_id)
    if user_update is None:
        raise HTTPException(status_code=404, detail="User not found")
    else:
        user_update.name = user.name
        user_update.password = pwd_context.hash(user.password)
        user_update.email = user.email
        user_update.username = user.username
        db.commit()


    return user_update
@route.delete("/{user_id}")
def delete_user(user_id: int) -> UserSchema:
    """
        Delete user selected by id
    """
    user = get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    else:
        db.delete(user)
        db.commit()

    return UserSchema(**user.__dict__)
