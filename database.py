from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session,sessionmaker



# Create a sqlite engine instance
engine = create_engine("sqlite:///QA_service.db")

# Create a DeclarativeMeta instance
Base = declarative_base()

# Create SessionLocal class from sessionmaker factory
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)


# Create the database
Base.metadata.create_all(engine)
