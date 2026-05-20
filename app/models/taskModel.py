from sqlalchemy import Column,Integer,String,SmallInteger,Text,ForeignKey,Date,func
from sqlalchemy.orm import relationship
from core.database import Base
from models.model import Status, Priority

class Tasks(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(150), nullable=False)
    description = Column(Text, nullable=True)
    is_deleted = Column(SmallInteger, default=0)
    start_date = Column(Date, default=func.sysdate())
    end_date = Column(Date, nullable=True)
    estimated_hours = Column(Integer, nullable=True)
    
    assignee_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    created_by = Column(Integer, ForeignKey("users.id"), nullable=False)
    status_id = Column(Integer, ForeignKey("status.id"), nullable=False)
    priority_id = Column(Integer, ForeignKey("priority.id"), nullable=False)
    request_status = Column(String(50), default="created")
    status_description = Column(String(255), nullable=True)

    assignee = relationship("Users",foreign_keys=[assignee_id],back_populates="assignee_task")
    creator = relationship("Users",foreign_keys=[created_by],back_populates="created_task")
    status = relationship(Status, back_populates="tasks")
    priority = relationship(Priority, back_populates="tasks")

