from . import models
from .database import engine, get_db
from fastapi import FastAPI, HTTPException, Response, status, Depends
from pydantic import BaseModel
# To retrieve name of column. Might not be needed in latest version
from psycopg2.extras import RealDictCursor
from sqlalchemy.orm import Session

import psycopg2
import time


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True


while True:
    try:
        conn = psycopg2.connect(
            host='localhost', database='fastapi', user='postgres', password='1234', cursor_factory=RealDictCursor)

        cursor = conn.cursor()
        print("Database connected...")

        break
    except Exception as error:
        print("Database connection failed")
        print("Error:", error)
        time.sleep(2)


@app.get("/")
def root():
    return {"message": "Welcome to my API!"}


@app.get("/sqlalchemy")
def test_posts(db: Session = Depends(get_db)):
    return {"status": "Success"}


@app.get("/posts")
def get_posts():
    cursor.execute("SELECT * FROM posts")
    posts = cursor.fetchall()

    return {"data": posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    cursor.execute(
        "INSERT INTO posts(title, content, published) VALUES(%s, %s, %s) RETURNING *",
        (post.title, post.content, post.published))

    new_post = cursor.fetchone()
    conn.commit()

    return {"data": new_post}


@app.get("/posts/{id}")
def get_post(id: int):
    cursor.execute("SELECT * FROM posts WHERE Id = %s", (str(id),))
    post = cursor.fetchone()

    if not post:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            f"Post with id: {id} was not found")

    return {"post_detail": post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    cursor.execute("DELETE FROM posts WHERE id = %s RETURNING *", (str(id),))
    deleted_post = cursor.fetchone()

    conn.commit()

    if deleted_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id {id} does not exist")

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    cursor.execute("UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *",
                   (post.title, post.content, post.published, str(id)))

    updated_post = cursor.fetchone()
    conn.commit()

    if updated_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id {id} does not exist")

    return {"data": updated_post}
