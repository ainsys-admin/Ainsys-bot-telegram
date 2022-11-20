import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime, String, BigInteger, ForeignKey, Boolean
from sqlalchemy.orm import relationship

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True

    id = Column(BigInteger, primary_key=True, autoincrement=True)


class Users(BaseModel):
    __tablename__ = 'users'
    user_id = Column(String(255), nullable=False)
    chat_id = Column(String(255), nullable=False)
    ainsys_webhook = (Column(String(255), nullable=False))


class Entities(BaseModel):
    __tablename__ = 'entities'
    entity = Column(String(255), nullable=False)
    chat_id = Column(String(255), nullable=False)
    user_id = (Column(String(255), nullable=False))


class Fields(BaseModel):
    __tablename__ = 'fields'
    field = Column(String(255), nullable=False)
    type_field = Column(String(255), nullable=False)
    entity_id = Column(String(255), nullable=False)
    chat_id = Column(String(255), nullable=False)
    user_id = (Column(String(255), nullable=False))
