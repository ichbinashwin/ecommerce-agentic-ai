from pydantic import BaseModel

class ProductBase(BaseModel):

    name: str
    brand: str
    category: str
    price: float
    description: str
    stock: int
    rating: float

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int
    class Config:
        from_attributes = True
