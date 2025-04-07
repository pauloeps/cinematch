from fastapi import APIRouter, Depends
from typing import Annotated

from app.services.user_service import update_user, get_current_user

from app.schemas.user import UserCreate, UserResponse
from app.models.user import User

router = APIRouter()


@router.get("/me")
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_user)],
):
    return UserResponse(
        id=current_user.id, nome=current_user.nome, email=current_user.email
    )


@router.put("/me", response_model=UserResponse)
def update_users_me(
    current_user: Annotated[User, Depends(get_current_user)],
    user: UserCreate,
):
    updated_user = update_user(current_user, user)
    return UserResponse(
        id=updated_user.id, nome=updated_user.nome, email=updated_user.email
    )
