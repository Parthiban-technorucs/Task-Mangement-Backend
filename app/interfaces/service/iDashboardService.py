from abc import ABC, abstractmethod

class IDashboardService(ABC):
    @abstractmethod
    def task_stats(self):
        pass
    
    @abstractmethod
    def user_stats(self):
        pass
