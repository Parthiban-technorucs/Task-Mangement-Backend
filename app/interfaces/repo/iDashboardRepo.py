from abc import ABC, abstractmethod

class IDashboardRepo(ABC):
    @abstractmethod
    def task_stats(self):
        pass
    
    @abstractmethod
    def user_stats(self):
        pass
