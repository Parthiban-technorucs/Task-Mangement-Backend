from fastapi import APIRouter
from schema.requestShema import TaskSchema
from typing import List
from dependencies.services import TaskServiceDep
from dependencies.auth import CurrentUserDep

route = APIRouter()

@route.get('/')
def get_tasks(service: TaskServiceDep, user: CurrentUserDep):
    return service.get_task(user["userid"])

@route.post('/create')
def create_task(task: TaskSchema, service: TaskServiceDep, user: CurrentUserDep):
    return service.save_task(task, user)

@route.put('/update')
def update_task_by_id(task: TaskSchema, service: TaskServiceDep):
    return service.update_task(task)

@route.delete('/delete')
def delete_task(ids: List[int], service: TaskServiceDep):
    return service.delete_task(ids)

@route.post('/assign')
def assign_task(user_id: int, task_id: int, service: TaskServiceDep):
    return service.assign_task(task_id, user_id)

@route.post('/update/status')
def update_status(task_id: int, status: int, service: TaskServiceDep):
    return service.update_status(task_id, status)
