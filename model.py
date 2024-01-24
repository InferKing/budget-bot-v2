from sqlalchemy import Table, Index, Integer, String, Column, Text, DateTime
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    tg_id = Column(String(12), nullable=False)
    username = Column(String(50), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    chat_data = relationship("Chat")

class Chat(Base):
    __tablename__ = 'chat_data'
    id = Column(Integer, primary_key=True)
    