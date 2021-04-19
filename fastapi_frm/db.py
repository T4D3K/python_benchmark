import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_url = os.environ.get('DB_URL', 'postgresql+psycopg2://postgres:postgres@db/postgres')
pool_size = int(os.environ.get('DB_POOL_SIZE', 20))
engine = create_engine(db_url, echo=False, pool_size=pool_size)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
