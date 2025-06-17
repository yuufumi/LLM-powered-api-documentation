from sqlalchemy import Column, Integer, String, Boolean
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer, index=True)
    is_admin = Column(Boolean, default=True)

    # Add relationships if needed

    def __repr__(self):
        return f"<Item(id={self.id}, title='{self.name}')>"