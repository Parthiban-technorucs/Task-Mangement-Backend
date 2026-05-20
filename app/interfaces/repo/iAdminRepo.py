from abc import ABC, abstractmethod

class IAdminRepo(ABC):
    @abstractmethod
    def get_all_users(self):
        pass
    
    @abstractmethod
    def get_all_tasks(self):
        pass
        
    @abstractmethod
    def delete_user(self, id):
        pass
    
    @abstractmethod
    def get_amdin_info(self, id):
        pass
    
    @abstractmethod
    def create_user(self, user):
        pass

    @abstractmethod
    def update_user_role(self, id, user):
        pass
    
    @abstractmethod
    def get_admin_details(self, id):
        pass
    
    @abstractmethod
    def get_pending_request(self):
        pass

    @abstractmethod
    def approve_status(self, task_id, status, description):
        pass