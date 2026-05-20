from typing import Annotated
from fastapi import Depends
from core.authentication import Auth

auth = Auth()

def get_current_user(user = Depends(auth.get_user)):
    return user

CurrentUserDep = Annotated[dict, Depends(get_current_user)]
