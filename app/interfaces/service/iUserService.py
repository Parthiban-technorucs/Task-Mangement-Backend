from abc import ABC, abstractmethod

class IUserService(ABC):
    @abstractmethod
    def get_user_info(self, id: int):
        pass
    
    @abstractmethod
    def update_user(self, id: int, name: str):
        pass
    
    @abstractmethod
    def get_priority(self):
        pass
    
    @abstractmethod
    def get_status(self):
        pass
