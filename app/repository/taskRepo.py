
from typing import Annotated
from fastapi import Depends, HTTPException
from core.database import get_db
from interfaces.repo.iTaskRepo import ITaskRepo
from models.taskModel import Tasks
from sqlalchemy.orm import Session
from sqlalchemy import or_


class TaskRepo(ITaskRepo):
    def __init__(self, db: Annotated[Session, Depends(get_db)]):
        self.db = db

    def save(self, task):
        db_task = Tasks(**task.model_dump())
        self.db.add(db_task)
        self.db.commit()
        self.db.refresh(db_task)
        return db_task

    def get_task_by_id(self, id):
        return self.db.query(Tasks).filter(or_(Tasks.created_by == id, Tasks.assignee_id == id)).all()

    def get_task_by_task_id(self, task_id):
        return self.db.query(Tasks).filter(Tasks.id == task_id).first()

    def update(self, task):
        db_task = self.db.query(Tasks).filter(Tasks.id == task.id).first()
        if db_task:
            for key, value in task.dict().items():
                setattr(db_task, key, value)
            self.db.commit()
            self.db.refresh(db_task)
        return db_task

    def delete(self, id):
        db_task = self.db.query(Tasks).filter(Tasks.id == id).first()
        if db_task:
            db_task.is_deleted = 1
            self.db.commit()
        return db_task

    def assign_task(self, task_id, user_id):
        db_task = self.db.query(Tasks).filter(Tasks.id == task_id).first()
        if db_task:
            db_task.assignee_id = user_id
            self.db.commit()
            self.db.refresh(db_task)
        return db_task
    
    def update_status(self, task_id, status):
        try:
            db_task = self.db.query(Tasks).filter(Tasks.id == task_id).first()
            if db_task:
                db_task.status_id = status
                db_task.request_status = "pending"
                self.db.commit()
                self.db.refresh(db_task)
            return db_task  
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))