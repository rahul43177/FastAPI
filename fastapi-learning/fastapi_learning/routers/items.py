from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from typing import List

from ..database import get_database
from ..models.item import Item
from ..schemas.item import ItemCreate, Item as ItemSchema

router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Item not found"}},
)

@router.post("/", 
    response_model=ItemSchema,
    status_code=status.HTTP_201_CREATED,
    responses={
        400: {"description": "Invalid input"},
        500: {"description": "Internal server error"}
    }
)
def create_item(item: ItemCreate, db: Session = Depends(get_database)):
    try:
        db_item = Item(**item.model_dump())
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while creating the item: {str(e)}"
        )

@router.get("/", 
    response_model=List[ItemSchema],
    responses={500: {"description": "Internal server error"}}
)
def read_items(
    skip: int = Query(default=0, ge=0, description="Number of items to skip"),
    limit: int = Query(default=100, ge=1, le=100, description="Number of items to return"),
    db: Session = Depends(get_database)
):
    try:
        items = db.query(Item).offset(skip).limit(limit).all()
        return items
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while fetching items: {str(e)}"
        )

@router.get("/{item_id}", 
    response_model=ItemSchema,
    responses={
        404: {"description": "Item not found"},
        500: {"description": "Internal server error"}
    }
)
def read_item(item_id: int, db: Session = Depends(get_database)):
    try:
        item = db.query(Item).filter(Item.id == item_id).first()
        if item is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Item with id {item_id} not found"
            )
        return item
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while fetching the item: {str(e)}"
        )

@router.put("/{item_id}", 
    response_model=ItemSchema,
    responses={
        404: {"description": "Item not found"},
        400: {"description": "Invalid input"},
        500: {"description": "Internal server error"}
    }
)
def update_item(item_id: int, item: ItemCreate, db: Session = Depends(get_database)):
    try:
        db_item = db.query(Item).filter(Item.id == item_id).first()
        if db_item is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Item with id {item_id} not found"
            )
        
        for key, value in item.model_dump().items():
            setattr(db_item, key, value)
        
        db.commit()
        db.refresh(db_item)
        return db_item
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while updating the item: {str(e)}"
        )

@router.delete("/{item_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        404: {"description": "Item not found"},
        500: {"description": "Internal server error"}
    }
)
def delete_item(item_id: int, db: Session = Depends(get_database)):
    try:
        db_item = db.query(Item).filter(Item.id == item_id).first()
        if db_item is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Item with id {item_id} not found"
            )
        
        db.delete(db_item)
        db.commit()
        return None
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while deleting the item: {str(e)}"
        ) 