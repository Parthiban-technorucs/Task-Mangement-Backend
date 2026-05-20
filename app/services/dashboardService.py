from typing import Annotated
from fastapi import Depends
from interfaces.service.iDashboardService import IDashboardService
from repository.userRepo import DashboardRepo
from fastapi import HTTPException

class DashboardService(IDashboardService):
    def __init__(self, repo: Annotated[DashboardRepo, Depends(DashboardRepo)]):
        self.repo = repo
        
    def task_stats(self):
        try:
            stats = self.repo.task_stats()
            return stats
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
    
    def user_stats(self):
        try:
            stats = self.repo.user_stats()
            return stats
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))