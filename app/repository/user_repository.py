from typing import List

from app.models.user import User
from app.schemas.user import UserCreate

users: List[User] = []


def create_user(user: UserCreate):
    id = len(users) + 1
    users.append(User(id=id, nome=user.nome, email=user.email, senha=user.senha))
    return user


def get_all_users():
    return users


def get_user_by_id(user_id: int) -> User:
    for user in users:
        if user.id == user_id:
            return user
    return None


def get_user_by_email(email: str):
    for user in users:
        if user.email == email:
            return user
    return None


def update_user(user_id: int, user: User) -> User:
    for i, u in enumerate(users):
        if u.id == user_id:
            updated_user = User(
                id=user_id, nome=user.nome, email=user.email, senha=user.senha
            )
            users[i] = updated_user
            return updated_user


def delete_user(user_id: int):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    return None
