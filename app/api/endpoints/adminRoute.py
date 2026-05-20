from fastapi import APIRouter
from typing import List
from schema.requestShema import RegisterSchema
from schema.responseShema import TaskDetailsResponse, UserResponse, AdminUserResponse, TaskStatusRequest
from dependencies.services import AdminServiceDep
from dependencies.auth import CurrentUserDep

route = APIRouter()

@route.get('/', response_model=UserResponse)
def get_admin(service: AdminServiceDep, user: CurrentUserDep):
    return service.get_admin_info(user["userid"])

@route.get('/users', response_model=List[AdminUserResponse])
def get_users(service: AdminServiceDep):
    return service.get_all_users()

@route.get('/tasks', response_model=List[TaskDetailsResponse])
def get_tasks(service: AdminServiceDep):
    return service.get_all_tasks()

@route.post('/users/create')
def create_user(user: RegisterSchema, service: AdminServiceDep):
    return service.create_user(user)

@route.post('/users/role')
def update_user_role(role_id: int, user_id: int, service: AdminServiceDep):
    return service.update_user_role_by_id(role_id, user_id)

@route.delete('/users/delete/{id}')
def delete_user(id: int, service: AdminServiceDep):
    return service.delete_user(id)

@route.get('/status/request', response_model=TaskStatusRequest)
def get_status_pendings(service: AdminServiceDep):
    return service.status_request()

@route.post('/status/update')
def update_status(task_id: int, status: int, description: str, service: AdminServiceDep):
    return service.approve_status(task_id, status, description)

