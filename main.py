from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel


app = FastAPI()

# class Post(BaseModel):
#   title:
#   content:

@app.get("/")
def root():
  return {"Message": "thon"}

@app.get("/posts")
def get_posts():
  return {"data":"Number of posts"}

@app.post("/createposts")
def create_posts(payload: dict = Body(...)):
  print(payload)
  return {"New_content" : f"title: {payload['title']} and the content: {payload['content']}"}

