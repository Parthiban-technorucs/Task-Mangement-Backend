
from datetime import date
from typing import Optional
from pydantic import BaseModel, ConfigDict

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    start_date: date
    end_date: Optional[date]
    estimated_hours: Optional[int]
    class Config:
        from_attributes = True
    
class StatusResponse(BaseModel):
    status_name: str
    class Config:
        from_attributes = True

class PriorityResponse(BaseModel):
    priority_name: str
    class Config:
        from_attributes = True
          
class UserResponse(BaseModel): 
    id: int
    user_name: str
    email: str
    role_name: Optional[str] = "user"
    model_config = ConfigDict(from_attributes=True)
    
class TaskDetailsResponse(BaseModel):
    Tasks: TaskResponse
    Users: UserResponse
    Status: StatusResponse
    Priority: PriorityResponse
    class Config:
        from_attributes = True  
        
        
class LoginResponse(BaseModel):
    user: UserResponse
    token: str
    class Config:
        from_attributes = True
        
class AdminUserResponse(BaseModel):
    id: int
    user_name: str
    class Config:
        from_attributes = True
        
class TaskStatusRequest(BaseModel):
    id: int
    title: str
    description: Optional[str]
    start_date: date
    end_date: Optional[date]
    estimated_hours: Optional[int]
    request_status: str
    class Config:
        from_attributes = True
        
class StatusResponses(BaseModel):
    id: int
    status_name: str
    class Config:
        from_attributes = True
        
class PriorityResponses(BaseModel):
    id: int
    priority_name: str
    class Config:
        from_attributes = True
    