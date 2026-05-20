from fastapi import APIRouter
from dependencies.services import DashboardServiceDep

route = APIRouter()

@route.get('/tasks')
def get_tasks_stats(service: DashboardServiceDep):
    return service.task_stats()

@route.get('/user')
def get_user_stats(service: DashboardServiceDep):
    return service.user_stats()
