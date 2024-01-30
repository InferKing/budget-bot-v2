from sqlalchemy import Table, Index, Integer, String, Column, Text, DateTime, ForeignKey
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
    chat_data = relationship("ChatBridge")

class ChatData(Base):
    __tablename__ = 'chat_data'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.tg_id"))
    role = Column(String(10), nullable=False, default="user")
    message = Column(Text, nullable=False)
    created_on = Column(DateTime(), default=datetime.now)

# select * from chat_data where user_id = '123';