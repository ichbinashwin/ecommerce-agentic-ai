from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from api.dependencies import get_db
from models.product import Product

from schemas.product import ProductResponse
from schemas.product import ProductCreate
from schemas.product import ProductUpdate

from typing import Optional

router = APIRouter()

@router.get(
    "/",
    response_model=list[ProductResponse]
)
async def get_products(
    db: Session = Depends(get_db)
):

    products = db.query(Product).all()

    return products

@router.get("/search")
def search_products(

    brand: Optional[str] = None,

    category: Optional[str] = None,

    min_price: Optional[float] = None,

    max_price: Optional[float] = None,

    db: Session = Depends(get_db)

):

    query = db.query(Product)

    if brand:
        query = query.filter(
            Product.brand.ilike(f"%{brand}%")
        )

    if category:
        query = query.filter(
            Product.category.ilike(f"%{category}%")
        )

    if min_price:
        query = query.filter(
            Product.price >= min_price
        )

    if max_price:
        query = query.filter(
            Product.price <= max_price
        )

    return query.all()

@router.get(
    "/{product_id}",
    response_model=ProductResponse
)
async def get_product(
    product_id: int,
    db: Session = Depends(get_db)
):

    product = db.query(Product).filter(
        Product.id == product_id
    ).first()

    return product

@router.put(

    "/{product_id}",

    response_model=ProductResponse

)
async def update_product(

    product_id: int,

    product: ProductUpdate,

    db: Session = Depends(get_db)

):

    existing_product = db.query(Product).filter(

        Product.id == product_id

    ).first()

    existing_product.name = product.name

    existing_product.price = product.price

    db.commit()

    db.refresh(existing_product)

    return existing_product

@router.delete("/{product_id}")
async def delete_product(
    product_id: int,
    db: Session = Depends(get_db)
):

    product = db.query(Product).filter(
        Product.id == product_id
    ).first()

    db.delete(product)

    db.commit()

    return {
        "message": "Product deleted successfully"
    }

@router.post(

    "/",

    response_model=ProductResponse

)
async def create_product(

    product: ProductCreate,

    db: Session = Depends(get_db)

):

    new_product = Product(

        name=product.name,

        price=product.price

    )

    db.add(new_product)

    db.commit()

    db.refresh(new_product)

    return new_product
