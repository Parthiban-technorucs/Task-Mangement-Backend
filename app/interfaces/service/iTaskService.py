from abc import ABC, abstractmethod

class ITaskService(ABC):
    @abstractmethod
    def save_task(self, task, user_id):
        pass
    
    @abstractmethod
    def update_task(self, task):
        pass
    
    @abstractmethod
    def delete_task(self, id: int):
        pass
    
    @abstractmethod
    def get_task(self, id: int):
        pass
    
    @abstractmethod
    def assign_task(self, task_id: int, user_id: int):
        pass

    @abstractmethod
    def update_status(self, task_id: int, status: int):
        pass
    