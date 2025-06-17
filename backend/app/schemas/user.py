from pydantic import BaseModel, Field
from typing import Optional

class UserBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    age: Optional[int] = None
    is_admin: bool = False

class UserCreate(UserBase):
    pass # Can add specific fields for creation if needed

class UserUpdate(UserBase):
    name: Optional[str] = None
    age: Optional[int] = None
    is_admin: Optional[bool] = None

class UserInDB(UserBase):
    id: int
    class ConfigDict:
        from_attributes = True # Allow ORM models to be converted to Pydantic models