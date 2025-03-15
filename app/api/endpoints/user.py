from fastapi import APIRouter, HTTPException
from app.services.user_service import (
    create_user,
    get_all,
    get_user,
    update_user,
    delete_user,
)
from app.schemas.user import UserCreate, UserResponse

router = APIRouter()


@router.post("/", response_model=UserResponse)
def register_user(user: UserCreate):
    return create_user(user)


@router.get("/", response_model=list[UserResponse])
def get_all_users():
    return get_all()


@router.get("/{user_id}", response_model=UserResponse)
def get_user_by_id(user_id: int):
    user = get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/{user_id}", response_model=UserResponse)
def update_user_by_id(user_id: int, user: UserCreate):
    existing_user = get_user(user_id)
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")
    return update_user(user_id, user)


@router.delete("/{user_id}")
def delete_user_by_id(user_id: int):
    existing_user = get_user(user_id)
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")
    delete_user(user_id)
    return {"message": "User deleted successfully"}
