from curses import echo
from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql://root:root@localhost/telemadb"

engin = create_engine(
    SQLALCHEMY_DATABASE_URL, echo=True
)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engin)

Base = declarative_base()

def get_db():
    db = session_local()
    try:
        return db
    finally:
        db.close()