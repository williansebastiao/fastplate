from fastapi import FastAPI
from sqlalchemy import create_engine, MetaData, Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://fastplate:123456@db/fastplate')
Base = declarative_base()
app = FastAPI()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(30))
    last_name = Column(String(100))
    email = Column(String(120), unique=True)
    avatar = Column(String(255), nullable=True)
    active = Column(Boolean, default=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime, nullable=True)
    address = relationship("Address", back_populates='user')


class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    zipcode = Column(String(8))
    city = Column(String(160))
    state = Column(String(2))
    number = Column(Integer)
    complement = Column(String(160), nullable=True)
    address = Column(String(100))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime, nullable=True)
    user = relationship("User", back_populates='address')


@app.get("/")
def index():
    return {"Hello": "World"}
