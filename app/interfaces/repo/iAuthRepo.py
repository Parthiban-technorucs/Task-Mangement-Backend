from abc import ABC, abstractmethod

class IAuthRepo(ABC):
    @abstractmethod
    def create(self, user):
        pass

    @abstractmethod
    def get_email(self, user):
        pass
