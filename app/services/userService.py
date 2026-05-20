from typing import Annotated
from fastapi import Depends, HTTPException
from interfaces.service.iUserService import IUserService
from repository.userRepo import UserRepo


class UserServices(IUserService):
    def __init__(self, repo: Annotated[UserRepo, Depends(UserRepo)]):
        self.repo = repo
    
    def get_user_info(self, id):
        try:
            user = self.repo.get_by_id(id)
            if not user:
                raise HTTPException(status_code=400, detail="User not found")
            return user
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    def update_user(self, id, name: str):
        try:
            user = self.repo.get_by_id(id)
            if not user:
                raise HTTPException(status_code=400, detail="User not found")
            
            updated_user = self.repo.update_user_name(user, name)
            return {"message": "User updated"}
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
        

    def get_status(self):
        try: 
            status =  self.repo.status()
            return status
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
            

    def get_priority(self):
        try:
            priority = self.repo.priority()
            return priority
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
