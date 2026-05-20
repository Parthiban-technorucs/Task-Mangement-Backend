from typing import Annotated
from fastapi import Depends, HTTPException
from interfaces.service.iTaskService import ITaskService
from repository.taskRepo import TaskRepo

class TaskService(ITaskService):
    def __init__(self, repo: Annotated[TaskRepo, Depends(TaskRepo)]):
        self.repo = repo

    def save_task(self, task, user_id):
        try:
            task.created_by = user_id
            db_task = self.repo.save(task)
            if not db_task:
                raise HTTPException(status_code=400, detail="Failed to create task")
            return {"message": "Task created successfully"}
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    def update_task(self, task):
        try:
            existing_task = self.repo.get_task_by_task_id(task.id)
            if not existing_task:
                raise HTTPException(status_code=400, detail="Task not found")
            
            db_task = self.repo.update(task)
            return {"message": "Task updated successfully"}
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    def get_task(self, id):
        try:
            tasks = self.repo.get_task_by_id(id)
            if not tasks:
                raise HTTPException(status_code=400, detail="No tasks found for this user")
            return tasks
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
        
    def delete_task(self, ids):
        try:
            for id in ids:
                existing_task = self.repo.get_task_by_task_id(id)
                if not existing_task:
                    raise HTTPException(status_code=400, detail=f"Task {id} not found")
                self.repo.delete(id)
            return {"message": "Task(s) deleted successfully"}
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
         
    def assign_task(self, task_id, user_id):
        try:
            existing_task = self.repo.get_task_by_task_id(task_id)
            if not existing_task:
                raise HTTPException(status_code=400, detail="Task not found")
            
            self.repo.assign_task(task_id, user_id)
            return {"message": "Task assigned successfully"}
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
        
    def status_update(self, task_id, status):
        try:
            existing_task = self.repo.get_task_by_task_id(task_id)
            if not existing_task:
                raise HTTPException(status_code=400, detail="Task not found")
            
            self.repo.update_status(task_id, status)
            return {"message": "Task status updated successfully"}
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))