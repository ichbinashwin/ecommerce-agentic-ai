# FastAPI Backend API

Backend REST APIs for MiniShop.

---

# Features

- Product APIs
- Swagger Documentation
- REST Architecture
- JSON Responses

---

# Run Backend

Create virtual environment:

python3 -m venv venv

Activate:

Mac/Linux:
source venv/bin/activate

Windows:
venv\Scripts\activate

---

# Install Dependencies

pip install fastapi uvicorn sqlalchemy

---

# Run Application

uvicorn main:app --reload

Runs on:
http://127.0.0.1:8000

Swagger:
http://127.0.0.1:8000/docs

---

# Example APIs

## Get Products

GET /api/v1/products/

---

## Create Product

POST /api/v1/products/

Example:

{
  "name": "Laptop",
  "price": 1200
}

---

# Folder Structure

app/
│
├── api/
├── models/
├── schemas/
├── database/
└── main.py

---

# Future Improvements

- PostgreSQL
- Authentication
- Pagination
- Search APIs
- Sorting
- Caching
- Rate Limiting
- API Gateway