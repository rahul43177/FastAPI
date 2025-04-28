from pydantic import BaseModel

class ItemBase(BaseModel):
    title: str
    description: str | None = None
    is_active: bool = True

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int

    class Config:
        from_attributes = True 