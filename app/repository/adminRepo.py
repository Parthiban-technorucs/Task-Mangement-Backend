from typing import Annotated
from fastapi import Depends, HTTPException
from core.database import get_db
from interfaces.repo.iAdminRepo import IAdminRepo
from models.userModel import Users
from sqlalchemy import select
from models.taskModel import Tasks
from models.model import Priority, Status

class AdminRepo(IAdminRepo):
    def __init__(self, db: Annotated[object, Depends(get_db)]):
        self.db = db

    def get_all_tasks(self):
        try:
            stmt = select(Tasks, Status, Priority, Users)\
                    .join(Status, Tasks.status_id == Status.id)\
                    .join(Priority, Priority.id == Tasks.priority_id)\
                    .join(Users, Users.id == Tasks.assignee_id)
            data = self.db.execute(stmt).mappings().all()
            return data

        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    def get_all_users(self):
        try:
            return self.db.query(Users).filter(Users.is_delete == 0).all()
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    def delete_user(self, id):
        try:
            db_user = self.db.query(Users).filter(Users.id == id, Users.is_delete == 0).first()
            if not db_user:
                raise HTTPException(status_code=400, detail="User not found")
            db_user.is_delete = 1
            self.db.commit()
            return True
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    def get_amdin_info(self, id):
        try:
            return self.db.query(Users).filter(Users.id == id, Users.is_delete == 0).first()
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    def create_user(self, user):
        try:
            existing_user = self.db.query(Users).filter(Users.email == user.email).first()
            
            if existing_user and existing_user.is_delete == 0:
                raise HTTPException(status_code=400, detail="User already exists")
            elif existing_user and existing_user.is_delete == 1:
                existing_user.is_delete = 0
                self.db.commit()
                self.db.refresh(existing_user)
                return
            else:
                db_user = Users(**user.model_dump())
                self.db.add(db_user)
                self.db.commit()
                self.db.refresh(db_user)
            return 
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    def update_user_role(self, role_id, user_id):
        try:
            db_user = self.db.query(Users).filter(Users.id == user_id, Users.is_delete == 0).first()
            if not db_user:
                raise HTTPException(status_code=400, detail="User not found")
            db_user.role_id = role_id
            self.db.commit()
            self.db.refresh(db_user)
            return 
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
        
    def get_admin_details(self, userid):
        try:
            db_user = self.db.query(Users).filter(Users.id == userid, Users.is_delete == 0).first()
            return db_user
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
        
    
    def get_pending_request(self):
        try:
            return self.db.query(Tasks).filter(Tasks.request_status == "pending")
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
        
        
    def approve_status(self, task_id, status, description):
        try:
            db_task = self.db.query(Tasks).filter(Tasks.id == task_id).first()
            if not db_task:
                raise HTTPException(status_code=400, detail="Task not found")
            db_task.status_id = status
            db_task.request_status = "approved"
            db_task.status_description = description
            self.db.commit()
            self.db.refresh(db_task)
            return 
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))