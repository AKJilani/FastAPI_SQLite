from sqlalchemy.orm import Session
from app import models, schemas
from app.core.security import hash_password

def create_user(db: Session, user: schemas.UserCreate):
    hashed_pw = hash_password(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_pw)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def get_users(db: Session):
    return db.query(models.User).all()