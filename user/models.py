from pydantic import BaseModel

class UserRegisterRequest(BaseModel):
    user_name: str
    password: str
    email: str


class UserRegisterResponse(BaseModel):
    user_name: str


class UserLoginResponse(BaseModel):
    user_name: str


class FailedRequest(BaseModel):
    message: str

class UserLoginRequest(BaseModel):
    user_name: str
    password: str
