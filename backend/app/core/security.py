from pwdlib import PasswordHash
import jwt
from datetime import datetime, timedelta, timezone
from app.core.config import settings

password_hash = PasswordHash.recommended()

def hash_password(password: str):
    return password_hash.hash(password)

def verify_password(password: str, h_password: str):
    return password_hash.verify(password, h_password)


def create_access_token(data: dict) -> str:
    payload = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    payload.update({"exp": expire, "type": "access"})
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
    return token

def create_refresh_token(data: dict) -> str:
    payload = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(days=7)
    payload.update({"exp": expire, "type": "refresh"})
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
    return token

def decode_token(token: str):
    return jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])