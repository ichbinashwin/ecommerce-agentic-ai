import os
import requests
from dotenv import load_dotenv
load_dotenv()
BASE_URL = os.getenv("PRODUCT_API")

def search_products(filters):
    response = requests.get(
        f"{BASE_URL}/products/search",
        params=filters
    )

    return response.json()
