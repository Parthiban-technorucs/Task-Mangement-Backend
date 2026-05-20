from abc import ABC, abstractmethod

class IUserRepo(ABC):
    @abstractmethod
    def get_by_id(self, id):
        pass
        
    @abstractmethod
    def get_user_task(self, id):
        pass
    
    @abstractmethod
    def priority(self):
        pass
    
    @abstractmethod
    def status(self):
        pass
