from sqlalchemy.orm import Session

from core.database import SessionLocal
from models.product import Product


db: Session = SessionLocal()

sample_products = [

    ("MacBook Air M2", 1199),
    ("MacBook Pro M3", 2499),
    ("iPhone 15", 999),
    ("iPhone 15 Pro", 1299),
    ("Samsung Galaxy S24", 1099),
    ("Dell XPS 15", 1899),
    ("Lenovo ThinkPad X1", 1799),
    ("Sony WH-1000XM5", 399),
    ("Apple Watch Ultra", 899),
    ("iPad Pro", 1399),
]

# Generate 100 products

products = []

for i in range(1, 101):

    name, price = sample_products[i % len(sample_products)]

    product = Product(
        name=f"{name} #{i}",
        price=price + i
    )

    products.append(product)

db.add_all(products)

db.commit()

print("100 products inserted successfully.")