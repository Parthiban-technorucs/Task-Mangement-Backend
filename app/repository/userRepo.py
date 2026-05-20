from typing import Annotated
from fastapi import Depends
from core.database import get_db
from interfaces.repo.iUserRepo import IUserRepo
from interfaces.repo.iDashboardRepo import IDashboardRepo
from models.userModel import Users
from models.model import Status, Priority
from models.taskModel import Tasks

class UserRepo(IUserRepo):
    def __init__(self, db: Annotated[object, Depends(get_db)]):
        self.db = db

    def get_by_id(self, id):
        return self.db.query(Users).filter(Users.id == id).first()

    def update_user_name(self, user, name: str):
        user.user_name = name
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_user_task(self, user):
        return self.db.query(Tasks).filter(Tasks.created_by == user).all()
    
    def status(self):
        return self.db.query(Status).all()
    
    def priority(self):
        return self.db.query(Priority).all()

class DashboardRepo(IDashboardRepo):
    def __init__(self, db: Annotated[object, Depends(get_db)]):
        self.db = db

    def task_stats(self):
        return self.db.query(Tasks).all()

    def user_stats(self):
        return self.db.query(Users).all() 
    

    
            