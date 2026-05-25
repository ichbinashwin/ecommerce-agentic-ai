# 🛒 MiniShop AI — LangGraph AI E-Commerce Assistant
![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![LangGraph](https://img.shields.io/badge/LangGraph-AgenticAI-orange)
![Gemini](https://img.shields.io/badge/Gemini-AI-red)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![Status](https://img.shields.io/badge/Status-MVP-success)
![License](https://img.shields.io/badge/License-MIT-yellow)
---
# 🚀 Overview
MiniShop AI is a lightweight AI-powered e-commerce application built using:
- FastAPI
- LangGraph
- Gemini AI
- Docker
- HTML/CSS/JavaScript
The project demonstrates how to build a conversational AI product assistant capable of understanding natural language product queries and dynamically rendering results in a frontend UI.
---
# ✨ Features
## Backend API
- FastAPI REST APIs
- Product CRUD endpoints
- SQLite database
- Swagger documentation
## AI Agent
- LangGraph workflow
- Gemini AI integration
- NLP-based product filtering
- Structured JSON responses
## Frontend
- AI product assistant
- Dynamic product rendering
- Query autocomplete
- Responsive UI
## DevOps
- Dockerized architecture
- Docker Compose orchestration
- Environment variable management
- GitHub-ready structure
---
# 🧠 Example Queries
```text
Show me products under 800
I want Apple products around 500
Show Samsung phones
Best rated headphones
```
⸻

🏗️ Architecture
```
Frontend UI
    ↓
AI Agent (LangGraph + Gemini)
    ↓
FastAPI Product APIs
    ↓
SQLite Database
```
⸻

🔄 LangGraph Workflow
```
START
  ↓
Receive User Query
  ↓
Extract NLP Filters
  ↓
Fetch Product Data
  ↓
Apply Dynamic Filters
  ↓
Return Structured JSON
  ↓
END
```
⸻

📦 Project Structure
```
ecommerce-api/
│
├── app/                  # FastAPI Backend APIs
├── ai-agent/             # LangGraph AI Agent
├── frontend/             # HTML/CSS/JS Frontend
│
├── docker-compose.yml
├── Makefile
├── README.md
├── LICENSE
├── SECURITY.md
└── CONTRIBUTING.md
```
⸻

⚙️ Tech Stack
```
Layer	Technology
Frontend	HTML, CSS, JavaScript
Backend API	FastAPI
AI Framework	LangGraph
Foundation Model	Gemini 2.5 Flash
Database	SQLite
Containerization	Docker
Orchestration	Docker Compose
```
⸻

🐳 Run With Docker
```
Clone Repository

git clone https://github.com/YOUR_USERNAME/ecommerce-ai-langgraph.git
cd ecommerce-ai-langgraph
```
⸻

Configure Environment Variables

Backend

Create:
```
app/.env
DATABASE_URL=sqlite:///./ecommerce.db
```
⸻

AI Agent

Create:
```
ai-agent/.env
GOOGLE_API_KEY=your_gemini_api_key
PRODUCT_API=http://backend-api:8000/api/v1
```
⸻

Start Application
```
docker compose up --build
```
⸻

🌐 Access Applications
```
Service	URL
Frontend	http://localhost:5500
Backend Swagger	http://localhost:8000/docs
AI Agent Swagger	http://localhost:9000/docs
```
⸻

🗃️ Seed Sample Products

Insert 100 sample products:
```
docker compose exec backend-api python seed_products.py
```
⸻

📚 API Example

Request
```
POST /chat
{
  "message": "Show Apple laptops under 1500"
}
```
⸻

Response
```
{
  "products": [
    {
      "id": 1,
      "name": "MacBook Air M2",
      "brand": "Apple",
      "category": "Laptop",
      "price": 1199,
      "rating": 4.8
    }
  ]
}
```
⸻

🔐 Security Notes

Never commit:

* .env
* API keys
* database files
* secrets
* tokens

Use:

* .env.example
* Docker secrets
* GitHub secret scanning

⸻

📈 Future Roadmap

AI Features

* Tool Calling
* Product Recommendations
* Multi-Agent Workflows
* Semantic Search
* Vector Database

Backend

* PostgreSQL
* Redis
* Authentication
* Pagination
* Search APIs

Frontend

* React / Next.js
* Streaming Responses
* Voice Search
* Chat History

DevOps

* Kubernetes
* CI/CD
* Terraform
* Monitoring
* Observability

⸻

🧪 Learning Objectives

This project demonstrates:

* AI orchestration architecture
* LangGraph workflows
* Conversational AI systems
* NLP filtering pipelines
* Dockerized microservices
* AI + frontend integration

⸻

🤝 Contributing

See:
```
CONTRIBUTING.md
```
⸻

🔒 Security

See:
```
SECURITY.md
```
⸻

📄 License

MIT License

⸻

⭐ Support

If you found this project useful:

* Star the repository
* Fork the project
* Contribute improvements

⸻

👨‍💻 Author
```
Ashwin Parmar

Security & Compliance Solutions Architect
Cloud | AI | Security | Software Architecture
```
