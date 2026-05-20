from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from core.config import DB_URL

engine = create_engine(DB_URL, pool_pre_ping=True)
session = sessionmaker(autoflush=True, bind=engine)

Base = declarative_base()

def get_db():
    db = session()
    try:
        yield db
    except Exception as e:
        db.rollback()
        raise
    finally:
        db.close()
