from fastapi import APIRouter
from api.v1.endpoints import products, users, orders
api_router = APIRouter()

api_router.include_router(
    products.router,
    prefix="/products",
    tags=["Products"]
)

api_router.include_router(
    users.router,
    prefix="/users",
    tags=["Users"]
)

api_router.include_router(
    orders.router,
    prefix="/orders",
    tags=["Orders"]
)
