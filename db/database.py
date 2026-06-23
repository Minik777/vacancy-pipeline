from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import create_engine
class Base(DeclarativeBase):
    pass

DB_URL = "sqlite:///vacancies.db"

engine = create_engine(DB_URL)

Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def init_db():
    Base.metadata.create_all(engine)



