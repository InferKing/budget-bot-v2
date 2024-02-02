<<<<<<< HEAD
from sqlalchemy import Integer, String, Column, Text, DateTime, ForeignKey
=======
from sqlalchemy import Table, Index, Integer, String, Column, Text, DateTime, ForeignKey
>>>>>>> 0c6d695c2716b2b4ca3ec3dbe0e475fba4260577
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
<<<<<<< HEAD
    chat_data = relationship("Chat", back_populates="user")

=======
    chat_data = relationship("ChatBridge")
>>>>>>> 0c6d695c2716b2b4ca3ec3dbe0e475fba4260577

class ChatData(Base):
    __tablename__ = 'chat_data'
    id = Column(Integer, primary_key=True)
<<<<<<< HEAD
    content = Column(Text, nullable=False)
    role = Column(String(10), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    created_on = Column(DateTime(), default=datetime.now)
    user = relationship("User", back_populates="chat_data")
=======
    user_id = Column(Integer, ForeignKey("users.tg_id"))
    role = Column(String(10), nullable=False, default="user")
    message = Column(Text, nullable=False)
    created_on = Column(DateTime(), default=datetime.now)

# select * from chat_data where user_id = '123' order by id;
>>>>>>> 0c6d695c2716b2b4ca3ec3dbe0e475fba4260577
