from abc import ABC, abstractmethod

class IAuthService(ABC):
    @abstractmethod
    def  register(self, response, user):
        pass
    
    @abstractmethod
    def login(self, response, user):
        pass
