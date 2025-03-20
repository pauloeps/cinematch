from app.models.user import User
from app.schemas.user import UserCreate

users = []


def create_user(user: UserCreate):
    id = len(users) + 1
    user.id = id
    users.append(user)
    return user


def get_all_users():
    return users


def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    return None


def update_user(user_id: int, user: User):
    for i, u in enumerate(users):
        if u.id == user_id:
            updated_user = User(
                id=user_id, nome=user.nome, email=user.email, senha=user.senha
            )
            users[i] = updated_user
            return updated_user
    return None


def delete_user(user_id: int):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    return None
