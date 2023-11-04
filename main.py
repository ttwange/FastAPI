from random import randrange
from fastapi import FastAPI, Response, status,HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional


app = FastAPI()

class Post(BaseModel):
  title: str
  content: str
  published: bool = True
  rating: Optional[int] = None

my_posts = [{"title": "title1","content":"content 1", "id":1},{"title": "title2","content":"content 2", "id":2}]
@app.get("/")
def root():
  return {"Message": "thon"}

def find_post(id):
  for p in my_posts:
    if p['id'] == id:
      return p

def find_index_post(id):
  for i, p in enumerate(my_posts):
    if p['id'] == id:
      return i

@app.get("/posts")
def get_posts():
  return {"data":my_posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post : Post):
 post_dict = post.dict()
 post_dict['id'] = randrange(0,3000000)
 my_posts.append(post_dict)
 return {"data": post_dict}

@app.get("/posts/{id}")
def get_post(id: int):
  post = find_post(id)
  if not post:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} not found")
  return {"post_detail": post} 

@app.delete("/posts/{id}")
def delete_post(id : int):
