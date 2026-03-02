from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from grocery_api.database import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)

    # Relationships
    products = relationship("Product", back_populates="category")
