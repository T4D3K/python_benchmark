from enum import Enum

from fastapi import FastAPI, Depends
import os
class ORMEnum(Enum):
    sqla = 'sqla'
    gino = 'gino'
    tort = 'tort'

ORM = Oros.environ.get('ORM', ORMEnum.sqla)
from sqlalchemy.orm import Session
from tortoise.contrib.fastapi import register_tortoise

from fastapi_frm import models
from fastapi_frm.db import engine, get_db
from pydantic import BaseModel

from fastapi_frm.gino_models import db, User as GUser
from fastapi_frm.tortoise_models import Users
app = FastAPI()
models.Base.metadata.create_all(bind=engine)

@app.get("/hello")
def read_root():
    return "hello world"

class UserModel(BaseModel):
    id: int = None
    name: str

    class Config:
        orm_mode = True


@app.post("/users", response_model=UserModel)
def users(user_data: UserModel, db: Session = Depends(get_db)):
    user = models.User(name=user_data.name)
    db.add(user)
    db.commit()
    user_data.id = user.id
    return user_data

@app.post("/ausers", response_model=UserModel)
async def update_user(user_data: UserModel):
    user = Users(name=user_data.name)
    await user.save()
    user_data.id = user.id
    return user_data

@app.post("/gusers", response_model=UserModel)
async def update_user(user_data: UserModel):
    rv = await GUser.create(name=user_data.name)
    user_data.id = rv.id
    return user_data

register_tortoise(
    app,
    db_url='postgres://postgres:postgres@db:5432/postgres',
    modules={"models": ["fastapi_frm.tortoise_models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

db.init_app(app)
