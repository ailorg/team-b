from sqlalchemy import Column,  String, DateTime, Integer, FetchedValue, Text
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
Base = declarative_base()


class WikiContent(Base):
    __tablename__ = 'wikicontents'

    id = Column("id", Integer, nullable=False, primary_key=True)
    class_name = Column("class_name", String(128), nullable=False)
    teacher = Column("teacher", String(128), nullable=True)
    text = Column("text", Text, nullable=True)
    date = Column("date", DateTime, default=datetime.now())

    @property
    def serialize(self):
        return {
            'class_name': self.class_name,
            'teacher': self.teacher,
            'text': self.text,
        }
