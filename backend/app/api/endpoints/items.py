from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from app.schemas.item import ItemCreate, ItemInDB, ItemUpdate
from app.crud import item as crud_item
from app.models.item import Item
# from app.core.security import get_current_user # If using authentication

router = APIRouter()

@router.post("/", response_model=ItemInDB, status_code=status.HTTP_201_CREATED)
async def create_item(item_in: ItemCreate): #, current_user: User = Depends(get_current_user)):
    # In a real app, you'd save to a DB
    db_item = await crud_item.create_item(item_in=item_in)
    return db_item

@router.get("/", response_model=List[ItemInDB])
async def read_items(): #, current_user: User = Depends(get_current_user)):
    items = await crud_item.get_all_items()
    return items

@router.get("/{item_id}", response_model=ItemInDB)
async def read_item(item_id: int):
    item = await crud_item.get_item(item_id=item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

# Add update and delete endpoints as needed