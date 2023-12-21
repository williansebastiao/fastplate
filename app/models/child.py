from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Child(Base):
    __tablename__ = 'children'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    first_name = Column(String(30))
    last_name = Column(String(100))
    gender = Column(String(2))
    birth = Column(Date)
    created_at = Column(DateTime, nullable=False, default=func.now())
    updated_at = Column(DateTime, null=True, default=func.now(), onupdate=func.now())
    deleted_at = Column(DateTime, nullable=True)
    user = relationship("User", back_populates="children")