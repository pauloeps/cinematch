from pydantic import BaseModel, EmailStr


class User(BaseModel):
    id: int
    nome: str
    email: EmailStr
    senha: str
