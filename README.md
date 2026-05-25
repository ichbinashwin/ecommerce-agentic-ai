# MiniShop AI E-Commerce

Simple E-Commerce Application with:

- FastAPI Backend
- HTML/CSS/JavaScript Frontend
- LangGraph AI Agent
- Gemini AI Integration

---

# Architecture

Frontend (HTML + JS)
    ↓
AI Agent (LangGraph + Gemini)
    ↓
FastAPI Product APIs
    ↓
PostgreSQL / SQLite

---

# Project Structure

ecommerce-api/
│
├── app/              # FastAPI Backend APIs
├── frontend/         # Frontend UI
├── ai-agent/         # LangGraph AI Agent
└── README.md

---

# Features

## Backend API
- Product CRUD APIs
- Swagger Documentation
- FastAPI Framework

## Frontend
- Product Listing UI
- AI Product Assistant
- Dynamic Product Rendering
- Query Autocomplete

## AI Agent
- LangGraph Workflow
- Gemini AI Integration
- Product Filtering
- Conversational Product Search

---

# Run Full Application

You need 3 terminals.

---

# Terminal 1 — Backend API

cd app

uvicorn main:app --reload

Runs on:
http://127.0.0.1:8000

Swagger:
http://127.0.0.1:8000/docs

---

# Terminal 2 — AI Agent

cd ai-agent

source venv/bin/activate

uvicorn main:api --reload --port 9000

Runs on:
http://127.0.0.1:9000

Swagger:
http://127.0.0.1:9000/docs

---

# Terminal 3 — Frontend

cd frontend

python3 -m http.server 5500

Open:
http://127.0.0.1:5500

---

# Future Improvements

- Real Tool Calling
- Product Recommendations
- Multi-Agent Architecture
- Authentication
- Docker
- PostgreSQL
- Redis Cache
- Vector Database
- Streaming Responses
- RAG Integration
- Kubernetes Deployment

---

# Tech Stack

- Python
- FastAPI
- LangGraph
- Gemini AI
- HTML
- CSS
- JavaScript

---

# Learning Goals

This project demonstrates:

- AI Agent Architecture
- Conversational APIs
- LangGraph Workflows
- Frontend + AI Integration
- Production AI Design Patterns