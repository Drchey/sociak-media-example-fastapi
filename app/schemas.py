from datetime import datetime
from pydantic import BaseModel, EmailStr
from pydantic.types import conint
from typing import Optional



class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    
    class Config: 
        orm_mode = True
        
class LoginUser(BaseModel):
    email: EmailStr
    password: str


class Post(BaseModel):
    title: str
    content: str
    is_published: bool = True
    owner: UserResponse

class PostBase(BaseModel):
    title: str
    content: str
    is_published: bool = True
    
class PostCreate(PostBase):
    pass

class PostResponse(PostBase):   
    created_at: datetime
    owner_id:int
    class Config:
        orm_mode = True
        


class Token(BaseModel):
    access_token: str
    token_type: str

class Token_Data(BaseModel):
    id: Optional[str] = None


class Vote(BaseModel):
    post_id : int
    dir: conint(le=1)