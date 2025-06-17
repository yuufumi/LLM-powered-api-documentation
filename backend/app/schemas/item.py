from pydantic import BaseModel, Field
from typing import Optional

class ItemBase(BaseModel):
    title: str = Field(..., min_length=3, max_length=50)
    description: Optional[str] = None
    is_active: bool = True

class ItemCreate(ItemBase):
    pass # Can add specific fields for creation if needed

class ItemUpdate(ItemBase):
    title: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None

class ItemInDB(ItemBase):
    id: int

    class ConfigDict:
        from_attributes = True # Allow ORM models to be converted to Pydantic models