from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.item import Item
from app.schemas.item import ItemCreate, ItemUpdate

async def get_item(db: AsyncSession, item_id: int):
    result = await db.execute(select(Item).where(Item.id == item_id))
    return result.scalar_one_or_none()

async def get_all_items(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(Item).offset(skip).limit(limit))
    return result.scalars().all()

async def create_item(db: AsyncSession, item_in: ItemCreate):
    db_item = Item(**item_in.model_dump())
    db.add(db_item)
    await db.commit()
    await db.refresh(db_item)
    return db_item

# Add update_item, delete_item functions