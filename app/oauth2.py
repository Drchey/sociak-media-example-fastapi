from jose import JWTError, jwt
from datetime import datetime, timedelta
from . import schemas, db, models
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .config import settings

oauth2scheme = OAuth2PasswordBearer(tokenUrl='login')

# SECRET KEY 
# ALGORITHM
# EXPIRATION

SECRET_KEY = settings.SECRET_KEY
ALGORITHM =  settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES

def create_access_token(data: dict()):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    
    encoded = jwt.encode(to_encode, SECRET_KEY, algorithm=[ALGORITHM])
    
    return encoded

def verify_token(token: str, cred_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
        id:str = payload.get("user_id")
        if id is None:
            raise cred_exception
        token_data = schemas.Token_Data(id =id)
    except JWTError:
        raise cred_exception
    return token_data
    

def get_current_user(token: str = Depends(oauth2scheme), db: Session = Depends(db.get_db)):
    cred_exception  = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Could Not Validate Credentials",
                                    headers={"WWW-Authenticate": "Bearer"}
                                    )
    token = verify_token(token, cred_exception)
    user = db.query(models.User).filter(models.User.id == token.id).first()
    return user
    
    
        
    
    