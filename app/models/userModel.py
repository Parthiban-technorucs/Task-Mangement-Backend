from sqlalchemy import Column,Integer,String,SmallInteger,Text,ForeignKey,Date,func
from sqlalchemy.orm import relationship
from core.database import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    user_name = Column(String(100), nullable=False)
    email = Column(String(150), nullable=False)
    password = Column(String(200), nullable=False)
    is_delete = Column(SmallInteger, default=0)
    
    role_id = Column(Integer, ForeignKey("role.id"), default=1)

    role = relationship("Role",back_populates="users")
    assignee_task = relationship("Tasks",foreign_keys="Tasks.assignee_id",back_populates="assignee")
    created_task = relationship("Tasks",foreign_keys="Tasks.created_by",back_populates="creator")
