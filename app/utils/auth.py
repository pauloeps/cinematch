import jwt
import redis
from datetime import datetime, timedelta, timezone


# Cliente do Redis para blacklist do token
redis_client = redis.Redis(host="localhost", port=6379, db=0, socket_timeout=5)

# Configurações do JWT, TODO: usar variaveis de ambiente
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(id: int) -> str:
    expire = datetime.now(tz=timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode = {"sub": str(id), "exp": expire}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_access_token(token: str) -> bool:
    try:
        # Verifica se está na blacklist
        if redis_client.get(f"blacklist:{token}"):
            return False

        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return True
    except jwt.ExpiredSignatureError:
        return False
    except jwt.PyJWTError:
        return False


def invalidate_token(token: str) -> bool:
    try:
        # Adiciona o token na blacklist com data de expiração
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        exp = payload.get("exp")
        if exp:
            ttl = exp - int(datetime.now(tz=timezone.utc).timestamp())
            if ttl > 0:
                try:
                    redis_client.setex(f"blacklist:{token}", ttl, "1")
                    return True
                except redis.RedisError:
                    return False
        return False
    except jwt.PyJWTError:
        return False
