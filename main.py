from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
  return {"Message": "thon"}

@app.get("/posts")
def get_posts():
  return {"data":"Number of posts"}

@app.post("/createposts")
def create_posts():
  return {"message":"successfully created posts"}