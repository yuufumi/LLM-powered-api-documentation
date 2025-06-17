from sqlalchemy import Column, Integer, String, Boolean
from app.core.database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    is_active = Column(Boolean, default=True)

    # Add relationships if needed

    def __repr__(self):
        return f"<Item(id={self.id}, title='{self.title}')>"