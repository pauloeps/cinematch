from typing import Annotated
from fastapi import Depends


from app.models.user import User
from app.schemas.user import UserCreate
from app.repository import user_repository
from app.utils.hash import hash_password
from app.utils.auth import decode_token, get_allowwed_token


def create_user(user: UserCreate):
    hashed_senha = hash_password(user.senha)
    user.senha = hashed_senha
    return user_repository.create_user(user)


def update_user(current_user: User, update_user: User):
    if update_user.senha:
        hashed_senha = hash_password(update_user.senha)
        update_user.senha = hashed_senha
    else:
        update_user.senha = current_user.senha
    return user_repository.update_user(current_user.id, update_user)


async def get_current_user(token: Annotated[str, Depends(get_allowwed_token)]):
    decoded = decode_token(token)
    user_id = int(decoded.get("sub"))
    user = user_repository.get_user_by_id(user_id)
    return user
