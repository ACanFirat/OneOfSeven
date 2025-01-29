from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from constants.constants import DATABASE_KEY

DATABASE_URL = DATABASE_KEY

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
