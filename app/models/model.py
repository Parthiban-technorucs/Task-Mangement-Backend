from sqlalchemy import Column,Integer,String,SmallInteger,Text,ForeignKey,Date,func
from sqlalchemy.orm import relationship
from core.database import Base


class Role(Base):
    __tablename__ = "role"
    id = Column(Integer, primary_key=True, autoincrement=True)
    role_name = Column(String(50), nullable=False)
    is_delete = Column(SmallInteger, default=0)
    users = relationship("Users", back_populates="role")

class Status(Base):
    __tablename__ = "status"
    id = Column(Integer, primary_key=True, autoincrement=True)
    status_name = Column(String(50), nullable=False)
    is_deleted = Column(SmallInteger, default=0)
    tasks = relationship("Tasks", back_populates="status")

class Priority(Base):
    __tablename__ = "priority"
    id = Column(Integer, primary_key=True, autoincrement=True)
    priority_name = Column(String(50), nullable=False)
    is_deleted = Column(SmallInteger, default=0)
    tasks = relationship("Tasks", back_populates="priority")
