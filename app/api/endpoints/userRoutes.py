from fastapi import APIRouter
from schema.responseShema import UserResponse, PriorityResponses, StatusResponses
from dependencies.services import UserServiceDep
from dependencies.auth import CurrentUserDep
from typing import List

route = APIRouter()

@route.get('/', response_model=UserResponse)
def get_user_details(service: UserServiceDep, user: CurrentUserDep):
    return service.get_user_info(user["userid"])

@route.put('/update')
def update_user_details(name: str, service: UserServiceDep, user: CurrentUserDep):
    return service.update_user(user["userid"], name)

@route.get('/status', response_model=List[StatusResponses])
def status(service: UserServiceDep):
    return service.get_status()

@route.get('/priority', response_model=List[PriorityResponses])
def status(service: UserServiceDep):
    return service.get_priority()
