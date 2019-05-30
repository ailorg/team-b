from sqlalchemy import Column,  String, DateTime, Integer, FetchedValue, Text, VARCHAR, CHAR,INT
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
Base = declarative_base()


class WikiContent(Base):
    __tablename__ = 'evaluation'

    id = Column("id", INT, nullable=False, primary_key=True)
    date = Column("date", DateTime, default=datetime.now(), nullable=True)
    class_name = Column("class_name", CHAR(20), nullable=True)
    score = Column("score",INT ,nullable=True)
    text = Column("text", VARCHAR(200), nullable=True)
    teacher = Column("teacher", CHAR(20), nullable=True)





    @property
    def serialize(self):
        return {
            'class_name': self.class_name,
            'teacher': self.teacher,
            'text': self.text,
        }
