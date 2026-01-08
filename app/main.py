import time


import psycopg2
from fastapi import FastAPI

# To retrieve name of column. Might not be needed in latest version
from psycopg2.extras import RealDictCursor

from . import models
from .database import engine
from .routers import post, user


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


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


app.include_router(post.router)
app.include_router(user.router)


@app.get("/")
def root():
    return {"message": "Welcome to my API!"}
