from typing import Annotated
from fastapi import Depends
from core.database import get_db
from interfaces.repo.iAuthRepo import IAuthRepo
from models.userModel import Users
from models.model import Role
from sqlalchemy.orm import Session, joinedload

class AuthRepo(IAuthRepo):
    def __init__(self, db: Annotated[Session, Depends(get_db)]):
        self.db = db

    def create(self, user):
        db_user = Users(**user.model_dump())
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user, ["role"])
        return db_user

    def get_email(self, email: str, password: str):
        return self.db.query(Users).options(joinedload(Users.role)).filter(Users.email == email, Users.password == password).first()

    def get_user_by_email(self, email: str):
        return self.db.query(Users).options(joinedload(Users.role)).filter(Users.email == email).first()

    def update_user_delete_status(self, user):
        user.is_delete = 0
        self.db.commit()
        self.db.refresh(user, ["role"])
        return user
     
