from sqlalchemy import Column, Integer, String, Boolean, CheckConstraint
from ..database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), index=True, nullable=False)
    description = Column(String(500))
    is_active = Column(Boolean, default=True, nullable=False)

    __table_args__ = (
        CheckConstraint('length(title) >= 3', name='check_title_length'),
    ) 