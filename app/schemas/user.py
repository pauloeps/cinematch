from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    nome: str
    email: EmailStr
    senha: str


class UserResponse(BaseModel):
    id: int
    nome: str
    email: EmailStr
