from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from grocery_api.database import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    address = Column(Text, nullable=False)
    phone = Column(String(50), nullable=False)

    # Relationships
    orders = relationship("Order", back_populates="customer")
