from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta, timezone

SECRET_KEY = "eu90234lksdvv345678ertyujjhgbfv98i1f3z2dh4tg6dy54fg4d5f6g7h8j9k0l1m2n3o4p5q6r7s8t9u0v1w2x3y4"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)