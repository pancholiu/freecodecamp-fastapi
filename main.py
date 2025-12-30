from fastapi import Body, FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Welcome to my API!"}


@app.get("/posts")
def get_posts():
    return {"data": "This is your post"}


@app.post("/createposts")
def create_posts(payLoad: dict = Body(...)):
    return {"new_post": f"title: {payLoad['title']} and content: {payLoad['content']}"}
