from abc import ABC, abstractmethod

class ITaskRepo(ABC):
    @abstractmethod
    def save(self, task):
        pass

    @abstractmethod
    def update(self, task):
        pass
    
    @abstractmethod
    def delete(self, id):
        pass
    
    @abstractmethod
    def get_task_by_id(self, id):
        pass
    
    @abstractmethod
    def assign_task(self, task_id, user_id):
        pass

    @abstractmethod
    def update_status(self, task_id, status):
        pass