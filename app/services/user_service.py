from app.models.user import User
from app.schemas.user import UserCreate
from app.repository import user_repository


def create_user(user: UserCreate):
    id = len(user_repository.get_all_users()) + 1
    new_user = User(id=id, nome=user.nome, email=user.email, senha=user.senha)
    return user_repository.create_user(new_user)


def get_all():
    return user_repository.get_all_users()


def get_user(user_id: int):
    return user_repository.get_user(user_id)


def update_user(user_id: int, user: User):
    return user_repository.update_user(user_id, user)


def delete_user(user_id: int):
    return user_repository.delete_user(user_id)
