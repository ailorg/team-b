from sqlalchemy import Column, Integer, String, Text, DateTime
from flaski.database import Base
from datetime import datetime


class WikiContent(Base):
    __tablename__ = 'wikicontents'
    id = Column(Integer, primary_key=True)
    class_name = Column(String(128))
    teacher = Column(String(128))
    text = Column(Text)
    date = Column(DateTime, default=datetime.now())

    def __init__(self, class_name=None, teacher=None, text=None, date=None):
        self.class_name = class_name
        self.teacher = teacher
        self.text = text
        self.date = date

    def __repr__(self):
        return '<Title %r>' % (self.title)
