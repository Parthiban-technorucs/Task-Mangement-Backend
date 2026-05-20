from typing import Annotated
from fastapi import Depends, HTTPException
from interfaces.service.iAuthService import IAuthService
from repository.authRepo import AuthRepo
from core.authentication import Auth
from schema.requestShema import LoginSchema
from schema.responseShema import LoginResponse, UserResponse
from interfaces.repo.iAuthRepo import IAuthRepo

set_user = Auth().set_cookie

AuthRepoDep = Annotated[IAuthRepo, Depends(AuthRepo)]


class AuthService(IAuthService):
    def __init__(self, repo: Annotated[AuthRepo, Depends(AuthRepo)]):
        self.repo = repo

    def register(self, response, user: LoginSchema):
        try:
            existing_user = self.repo.get_user_by_email(user.email)
            
            if existing_user and existing_user.is_delete == 0:
                raise HTTPException(status_code=400, detail="Email already exists")
            elif existing_user and existing_user.is_delete == 1:
                db_user = self.repo.update_user_delete_status(existing_user)
            else:
                db_user = self.repo.create(user)
            
            token = set_user(response, {"userid": db_user.id, "role": db_user.role.role_name})
                
            user_response:UserResponse = UserResponse.from_orm(db_user)
            return {"user": user_response, "token": token}
        
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    def login(self, response, user):
        try:
            db_user = self.repo.get_email(user.email, user.password)
            
            if not db_user:
                raise HTTPException(status_code=400, detail="Invalid email or password")
            
            user_response:UserResponse = UserResponse.model_validate(db_user)
            user_response.role_name = db_user.role.role_name

            token = set_user(response, {"userid": db_user.id, "role": db_user.role.role_name})
            login_response = LoginResponse(user=user_response, token=token)    
            return login_response
        
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
