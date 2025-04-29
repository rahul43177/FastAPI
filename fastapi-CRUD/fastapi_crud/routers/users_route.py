from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models.user_model import User
from schemas.user_schema import UserCreate, UserResponse
from service.crud import (
    create_user,
    get_all_users,
    get_user_by_id,
    update_user_details,
    delete_user
)

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

@router.post(
    "/",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new user"
)
async def create_user_route(
    user: UserCreate,
    db: Session = Depends(get_db)
) -> UserResponse:
    try:
        return create_user(db=db, user=user)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.get(
    "/",
    response_model=List[UserResponse],
    summary="Get all users"
)
async def get_all_users_route(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
) -> List[UserResponse]:
    return get_all_users(db=db, skip=skip, limit=limit)

@router.get(
    "/{user_id}",
    response_model=UserResponse,
    summary="Get user by ID"
)
async def get_user_by_id_route(
    user_id: int,
    db: Session = Depends(get_db)
) -> UserResponse:
    user = get_user_by_id(db=db, user_id=user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found"
        )
    return user

@router.put(
    "/{user_id}",
    response_model=UserResponse,
    summary="Update user by ID"
)
async def update_user_route(
    user_id: int,
    user: UserCreate,
    db: Session = Depends(get_db)
) -> UserResponse:
    updated_user = update_user_details(db=db, user_id=user_id, user=user)
    if not updated_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found"
        )
    return updated_user

@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete user by ID"
)
async def delete_user_route(
    user_id: int,
    db: Session = Depends(get_db)
) -> None:
    deleted = delete_user(db=db, user_id=user_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found"
        )
