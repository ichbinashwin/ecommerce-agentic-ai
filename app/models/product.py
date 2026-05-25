from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Text
)
from core.database import Base

class Product(Base):

    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    brand = Column(String, nullable=False)
    category = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    description = Column(Text)
    stock = Column(Integer, default=0)
    rating = Column(Float, default=0)
