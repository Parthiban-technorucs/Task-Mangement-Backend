from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date

class TaskSchema(BaseModel):
    title: str
    description: Optional[str] = None
    assignee_id: Optional[int] = None
    status_id: int
    priority_id: int
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    estimated_hours: Optional[int] = None


class RegisterSchema(BaseModel):
    user_name: str 
    email: EmailStr
    password: str 

class LoginSchema(BaseModel):
    email: EmailStr
    password: str
