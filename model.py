from sqlalchemy import Integer, String, Column, Text, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    tg_id = Column(String(12), nullable=False, unique=True)
    username = Column(String(50), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    chat_data = relationship("Chat", back_populates="user")


class Chat(Base):
    __tablename__ = 'chat_data'
    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    role = Column(String(10), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    created_on = Column(DateTime(), default=datetime.now)
    user = relationship("User", back_populates="chat_data")
