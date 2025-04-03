from app.schemas.auth import AuthLogin, AuthResponse
from app.repository import user_repository
from app.utils.hash import verify_password
from app.utils.auth import create_access_token, verify_access_token, invalidate_token
from fastapi import HTTPException, status


def login(auth: AuthLogin):
    user = user_repository.get_user_by_email(auth.email)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciais inválidas"
        )

    if not verify_password(auth.senha, user.senha):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciais inválidas"
        )

    access_token = create_access_token(user.id)
    return AuthResponse(access_token=access_token)


def logout(token: str):
    if not verify_access_token(token):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido"
        )

    if not invalidate_token(token):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Não foi possível invalidar o token",
        )

    return {"message": "Logout realizado com sucesso"}
