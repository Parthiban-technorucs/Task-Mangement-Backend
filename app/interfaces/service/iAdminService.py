from abc import ABC, abstractmethod

class IAdminService(ABC):
    @abstractmethod
    def get_admin_info(self, id: int):
        pass
    
    @abstractmethod
    def get_all_tasks(self):
        pass
    
    @abstractmethod
    def get_all_users(self):
        pass

    @abstractmethod
    def delete_user(self, id: int):
        pass
        
    @abstractmethod
    def create_user(self, user):
        pass
    
    @abstractmethod
    def update_user_role_by_id(self, id: int, user):
        pass

    @abstractmethod
    def status_request(self):
        pass
    
    @abstractmethod
    def approve_status(self, task_id, status, description):
        pass