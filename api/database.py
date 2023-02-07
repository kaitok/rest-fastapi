from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

username = os.environ.get("POSTGRES_USER")
password = os.environ.get("POSTGRES_PASSWORD")
database = os.environ.get("POSTGRES_DB")
host = os.environ.get("HOST")
port = os.environ.get("PORT")

SQLALCHEMY_DATABASE_URL = f"postgresql://{username}:{password}@{host}:{port}/{database}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
