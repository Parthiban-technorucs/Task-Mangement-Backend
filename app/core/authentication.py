from fastapi import Depends, Request, Response
from fastapi import HTTPException

from utils.security import verify_token, create_token
from core.config import jwt_token_name
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

security = HTTPBearer()

class Auth:
    def get_user(self, credentials: HTTPAuthorizationCredentials = Depends(security)):
        try:
            token = credentials.credentials
            if not token:
                raise HTTPException(status_code=401,detail="Unauthorized")
            payload = verify_token(token)
            return payload
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(status_code=400,detail=str(e))

    def set_cookie(self, response: Response, user_info):
        try:
            token = create_token(user_info)
            response.set_cookie(key=jwt_token_name,value=token)
            return token

        except Exception as e:
            raise HTTPException(status_code=400,detail=str(e))  