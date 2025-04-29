from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..crud import user_crud
from ..schemas import user_schema

router = APIRouter()

@router.get("/{user_id}", response_model=user_schema.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = user_crud.get_user_by_id(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.get("/", response_model=List[user_schema.User])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = user_crud.get_all_users(db, skip=skip, limit=limit)
    return users

@router.post("/", response_model=user_schema.User)
def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    db_user = user_crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_crud.create_user(db=db, user=user)

@router.put("/{user_id}", response_model=user_schema.User)
def update_user(user_id: int, user: user_schema.UserCreate, db: Session = Depends(get_db)):
    db_user = user_crud.get_user_by_id(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user_crud.update_user_details(db=db, user_id=user_id, user=user)

@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = user_crud.get_user_by_id(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    user_crud.delete_user(db=db, user_id=user_id)
    return {"message": "User deleted successfully"} 