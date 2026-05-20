from fastapi import APIRouter
from schema.responseShema import LoginResponse
from schema.requestShema import LoginSchema, RegisterSchema
from fastapi.responses import Response
from dependencies.services import AuthServiceDep
from dependencies.auth import CurrentUserDep

route = APIRouter()

@route.get('/')
def user_authenticate(user: CurrentUserDep):
    return {user["role"]}

@route.post('/signup')
def sign_up(user: RegisterSchema, response: Response, service: AuthServiceDep):
    return service.register(response, user)

@route.post('/login', response_model=LoginResponse)
def user_login(user: LoginSchema, response: Response, service: AuthServiceDep):
    return service.login(response, user)
