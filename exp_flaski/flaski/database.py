from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
Base = declarative_base()
mysql_url = 'mysql://root:password@0.0.0.0/psi?charset=utf8mb4'
engine = create_engine(mysql_url)
Base.metadata.bind = engine
session = sessionmaker(bind=engine)
db = session()


def init_db():
    import flaski.models
    Base.metadata.create_all(bind=engine)
