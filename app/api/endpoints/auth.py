from fastapi import APIRouter, Depends
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm


from app.services.auth_service import login, logout
from app.schemas.auth import AuthResponse, LogoutResponse
from app.services.user_service import create_user
from app.schemas.user import UserCreate, UserResponse

router = APIRouter()


@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate):
    return create_user(user)


@router.post("/login", response_model=AuthResponse)
def make_login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    return login(form_data)


@router.get("/logout", response_model=LogoutResponse)
def make_logout(token: str):
    return logout(token)
