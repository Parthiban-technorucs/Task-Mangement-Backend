from typing import Annotated
from fastapi import Depends, HTTPException
from interfaces.service.iAdminService import IAdminService
from repository.adminRepo import AdminRepo

class AdminServices(IAdminService):
    def __init__(self, repo: Annotated[AdminRepo, Depends(AdminRepo)]):
        self.repo = repo

    def get_admin_info(self, id):
        try:
            admin = self.repo.get_admin_details(id)
            if not admin:
                raise HTTPException(status_code=400, detail="Admin not found")
            if admin.is_delete == 1:
                raise HTTPException(status_code=400, detail="Admin not found")
            return admin
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    def get_all_tasks(self):
        try:
            tasks = self.repo.get_all_tasks()
            return tasks
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    def get_all_users(self):
        try:
            users = self.repo.get_all_users()
            if not users:
                raise HTTPException(status_code=400, detail="No users found")
            return users
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    def delete_user(self, id):
        try:
            user = self.repo.get_user_by_id(id)
            if not user:
                raise HTTPException(status_code=400, detail="User not found")
            if user.is_delete == 1:
                raise HTTPException(status_code=400, detail="User already deleted")
            self.repo.delete_user(id)
            return {"message": "User deleted"}
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    def create_user(self, user):
        try:
            existing_user = self.repo.get_all_users()
            for existing in existing_user:
                if existing.email == user.email and existing.is_delete == 0:
                    raise HTTPException(status_code=400, detail="User already exists")
            
            created_user = self.repo.create_user(user)
            return {"message": "User created successfully"}
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    def update_user_role_by_id(self, role_id, user_id):
        try:
            user = self.repo.get_user_by_id(user_id)
            if not user:
                raise HTTPException(status_code=400, detail="User not found")
            if user.is_delete == 1:
                raise HTTPException(status_code=400, detail="User not found")
            
            self.repo.update_user_role(role_id, user_id)
            return {"message": "User role updated successfully"}
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
        
        
    def status_request(self):
        try:
            update_requests = self.repo.get_pending_request()
            return update_requests
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
        
    def approve_status(self, task_id, status, description):
        try:
            self.repo.status_approved(task_id, status, description)
            return {"message": "Status updated successfully"}
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))


