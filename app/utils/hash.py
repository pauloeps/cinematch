import bcrypt


def hash_password(pw: str) -> str:
    salt = bcrypt.gensalt()
    hashed_pw = bcrypt.hashpw(pw.encode(), salt)
    return hashed_pw


def verify_password(pw: str, hashed_pw: str) -> bool:
    return bcrypt.checkpw(pw.encode(), hashed_pw.encode())
