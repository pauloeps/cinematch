from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    id: int | None = None
    nome: str
    email: EmailStr
    senha: str


class UserResponse(BaseModel):
    id: int
    nome: str
    email: EmailStr
