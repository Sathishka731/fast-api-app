from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str


app = FastAPI()


@app.get("/")
async def root():
    print("Hello World")
    return {"message": "Hello World"}


@app.get("/user/{userid}")
async def get_user(userid: int):
    return {"userid": userid}

@app.post("/adduser")
async def add_user(user: User):
    return user