from pydantic import BaseModel

class UserRegisterRequest(BaseModel):
    user_name: str
    password: str
    email: str


class UserLoginRequest(BaseModel):
    user_name: str
    password: str
