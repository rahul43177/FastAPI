from pydantic import BaseModel, Field, field_validator
from typing import Optional

class ItemBase(BaseModel):
    title: str = Field(..., min_length=3, max_length=100, description="Title of the item")
    description: Optional[str] = Field(None, max_length=500, description="Description of the item")
    is_active: bool = Field(default=True, description="Whether the item is active")

    @field_validator('title')
    @classmethod
    def title_must_be_valid(cls, v):
        if not v.strip():
            raise ValueError('Title cannot be empty or just whitespace')
        return v.strip()

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int = Field(..., description="The unique identifier for the item")

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "title": "Example Item",
                "description": "This is an example item",
                "is_active": True
            }
        } 