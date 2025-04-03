from fastapi import APIRouter
from app.services.auth_service import login, logout
from app.schemas.auth import AuthLogin, AuthResponse, LogoutResponse

router = APIRouter()


@router.post("/login", response_model=AuthResponse)
def make_login(auth: AuthLogin):
    return login(auth)


@router.get("/logout", response_model=LogoutResponse)
def make_logout(token: str):
    return logout(token)
