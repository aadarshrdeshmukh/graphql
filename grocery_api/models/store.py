from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from grocery_api.database import Base


class Store(Base):
    __tablename__ = "stores"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    address = Column(Text, nullable=False)
    opening_hours = Column(String(255), nullable=False)

    # Relationships
    inventory = relationship("Inventory", back_populates="store", cascade="all, delete-orphan")
    orders = relationship("Order", back_populates="store")
