from fastapi import Depends
from core.authentication import Auth
from fastapi import HTTPException

get_user = Auth().get_user

class RoleChecker:
    def __init__(self, allowedRole:list[str]):
        self.allowedRoles =  allowedRole
        
    def __call__(self, user =  Depends(get_user)):
        if user["role"] not in self.allowedRoles:
            raise HTTPException(status_code=401, detail="Access Denied")    
        return user       
 