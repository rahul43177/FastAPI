from fastapi import APIRouter , Depends , HTTPException
from sqlalchemy import Session
from typing import List

from ..database import get_database
from ..models.users import User
from ..schemas.user_schema import UserCreate , UserResponse as UserSchema

router = APIRouter(
    prefix= "/users/" , 
    tags = ['users']
)

@router.post("/" , response_model = UserSchema)
async def create_new_user(user : UserCreate , db : Session= Depends(get_database)): 
    db_item = User(**user.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


@router.get("/" , response_model = List[UserSchema])
async def get_all_users_data(skip : int = 0 , limit : int = 0 , db : Session = Depends(get_database)):
    users = db.query(User).offset(skip).limit(limit).all()
    return users

@router.get("/{user_id}" , response_model = UserSchema)
async def get_user_by_id(user_id : int , db:Session = Depends(get_database)):
    user = db.query(User).filter(User.id == user_id).first()

    if user is None : 
        raise HTTPException(status_code = 404 , detail = "User does not exist , wrong user id")
    return user 


@router.put("/{user_id}" , response_model = UserSchema)
async def update_user_data(user_id : int , user : UserCreate , db : Session = Depends(get_database)):
    user_in_database = db.query(User).filter(User.id == user_id).first()
    if user_in_database is None : 
        raise HTTPException(status_code = 404 , detail = "The user is not present in the database")
    for key , value in user.model_dump().items():
        setattr(user_in_database , key , value)
    
    db.commit()
    db.refresh(user_in_database)
    return user_in_database

        
#deleting 
@router.delete("/{user_id}") 
async def delete_user(user_id : int , db : Session = Depends(get_database)):
    user_in_database = db.query(User).filter(User.id == user_id).first()
    if user_in_database is None:
        raise HTTPException(
            status_code = 404 , 
            detail="The user is not present"
        )
    db.delete(user_in_database)
    db.commit()
    return {"message" : "The user has been deleted."}
    

    