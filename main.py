from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Post(BaseModel):
  title: str
  content: str
  published: bool = True
  rating: Optional[int] = None

@app.get("/")
def root():
  return {"Message": "thon"}

@app.get("/posts")
def get_posts():
  return {"data":"Number of posts"}

@app.post("/createposts")
def create_posts(post : Post):
  print(post)
  print(post.dict())
  return {"data": post}

