from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base


def init_db(db_path="sqlite:///app/db/harmony.sqlite"):
    engine = create_engine(db_path)
    Base.metadata.create_all(engine)
    return engine


Session = sessionmaker(bind=init_db())
