from pydantic import BaseModel, EmailStr


class AuthLogin(BaseModel):
    username: EmailStr
    password: str


class AuthResponse(BaseModel):
    access_token: str
    token_type: str


class LogoutResponse(BaseModel):
    message: str
