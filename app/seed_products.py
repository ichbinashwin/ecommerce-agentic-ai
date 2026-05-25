from sqlalchemy.orm import Session

from core.database import SessionLocal
from models.product import Product

db: Session = SessionLocal()

products = []

sample_products = [

    {
        "name": "MacBook Air M2",
        "brand": "Apple",
        "category": "Laptop",
        "price": 1199,
        "description": "Apple lightweight laptop",
        "stock": 25,
        "rating": 4.8
    },

    {
        "name": "MacBook Pro M3",
        "brand": "Apple",
        "category": "Laptop",
        "price": 2499,
        "description": "Apple professional laptop",
        "stock": 15,
        "rating": 4.9
    },

    {
        "name": "iPhone 15",
        "brand": "Apple",
        "category": "Phone",
        "price": 999,
        "description": "Apple smartphone",
        "stock": 40,
        "rating": 4.7
    },

    {
        "name": "Galaxy S24",
        "brand": "Samsung",
        "category": "Phone",
        "price": 899,
        "description": "Samsung flagship phone",
        "stock": 50,
        "rating": 4.6
    },

    {
        "name": "Dell XPS 15",
        "brand": "Dell",
        "category": "Laptop",
        "price": 1799,
        "description": "Dell premium ultrabook",
        "stock": 20,
        "rating": 4.5
    },

    {
        "name": "Sony WH-1000XM5",
        "brand": "Sony",
        "category": "Headphones",
        "price": 399,
        "description": "Noise cancelling headphones",
        "stock": 60,
        "rating": 4.9
    }
]

for i in range(1, 101):

    item = sample_products[i % len(sample_products)]

    product = Product(
        name=f"{item['name']} #{i}",
        brand=item["brand"],
        category=item["category"],
        price=item["price"] + i,
        description=item["description"],
        stock=item["stock"] + i,
        rating=item["rating"]
    )

    products.append(product)

db.add_all(products)
db.commit()
print("100 products inserted successfully.")
