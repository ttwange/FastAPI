from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel


app = FastAPI()

class Post(BaseModel):
  title: str
  content: str
  published: bool = True

@app.get("/")
def root():
  return {"Message": "thon"}

@app.get("/posts")
def get_posts():
  return {"data":"Number of posts"}

@app.post("/createposts")
def create_posts(new_post : Post):
  print(new_post.title)
  print(new_post.content)
  return {"data": "new post"}

