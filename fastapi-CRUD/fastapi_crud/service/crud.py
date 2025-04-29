from sqlalchemy.orm import Session
from models import user_model
from schemas import user_schema

def get_user_by_id(db: Session, user_id: int):
    return db.query(user_model.User).filter(user_model.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(user_model.User).filter(user_model.User.email == email).first()

def get_all_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(user_model.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: user_schema.UserCreate):
    db_user = user_model.User(
        email=user.email,
        name=user.name,
        age=user.age
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user_details(db: Session, user_id: int, user: user_schema.UserCreate):
    db_user = get_user_by_id(db, user_id)
    if db_user:
        for key, value in user.dict().items():
            setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = get_user_by_id(db, user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user