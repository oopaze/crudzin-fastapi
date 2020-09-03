from passlib.context import CryptContext
from fastapi import FastAPI

from .db import Base, engine

#Creating Encrypt/Decrypt object
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_app():
    """
        Creating and configuring our app
    """

    #Creating the API app
    app = FastAPI()

    #Importing routes will include to our app
    from .users.routes import route as user_route

    #Creating Database
    Base.metadata.create_all(bind=engine)

    #Including users routes to our app
    app.include_router(user_route,
                       prefix="/users",
                       tags=['User'],
                       responses={404: {"description": "Not found"}})

    return app
