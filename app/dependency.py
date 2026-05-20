from typing import Annotated
from fastapi import Depends
from services.authService import AuthService
from interfaces.service.iAuthService import IAuthService

def get_auth_service():
    return AuthService()

    