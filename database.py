from sqlalchemy import create_engine, Column, Integer, String 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session,sessionmaker

URL_DATABASE = 'postgresql://postgres:jerba_midoun0208@localhost:5432/QA_services'

# Create a sqlite engine instance
engine = create_engine(URL_DATABASE)

# Create a DeclarativeMeta instance
Base = declarative_base()

# Create SessionLocal class from sessionmaker factory
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)


# Create the database
Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally :
        db.close()