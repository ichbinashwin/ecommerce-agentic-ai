import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("PRODUCT_API")


def get_products():
    response = requests.get(f"{BASE_URL}/products/")
    return response.json()