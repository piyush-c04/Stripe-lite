# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
import os
from dotenv import load_dotenv

# Load the environment variables from .env file
load_dotenv()

# Database URL connection
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    print("Database URL not found. Please set the DATABASE_URL environment variable.")
else:
    engine = create_engine(DATABASE_URL)


# ✅ SQLAlchemy 2.0 declarative base
class Base(DeclarativeBase):
    pass

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()