from pydantic import BaseModel, EmailStr


class AuthLogin(BaseModel):
    email: EmailStr
    senha: str


class AuthResponse(BaseModel):
    access_token: str


class LogoutResponse(BaseModel):
    message: str
