from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import time
import psycopg2
# To retrieve name of column. Might not be needed in latest version
from psycopg2.extras import RealDictCursor
from .config import settings

SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{settings.DATABASE_USERNAME}:"
    f"{settings.DATABASE_PASSWORD}@"
    f"{settings.DATABASE_HOSTNAME}:"
    f"{settings.DATABASE_PORT}/"
    f"{settings.DATABASE_NAME}"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# while True:
#     try:
#         conn = psycopg2.connect(
#             host='localhost', database='fastapi', user='postgres', password='1234', cursor_factory=RealDictCursor)

#         cursor = conn.cursor()
#         print("Database connected...")

#         break
#     except Exception as error:
#         print("Database connection failed")
#         print("Error:", error)
#         time.sleep(2)
