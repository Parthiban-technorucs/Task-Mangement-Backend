from jose import jwt, JWTError
import json
from core.config import secret_key
from fastapi import HTTPException
from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["bcrypt"],
)

def create_token(userInfo):
    try:
        token = jwt.encode(userInfo, secret_key)
        return token
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) 

def verify_token(token):
    try:
        payload = jwt.decode(token, secret_key)
        return payload
    except JWTError as e:
        raise HTTPException(status_code=401, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

def hash_password(plain_password):
    try:
        if not plain_password:
            raise ValueError("The empty password")
        hashed_password = pwd_context.hash(plain_password)
        return hashed_password
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
