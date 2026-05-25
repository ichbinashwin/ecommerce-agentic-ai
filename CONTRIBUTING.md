# Contributing Guidelines

Thank you for contributing.

---

# Development Setup

## Clone Repository
```
git clone <repo-url>

cd ecommerce-agentic-ai
```
---

# Backend
```
cd app

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```
---

# AI Agent
```
cd ai-agent

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```
---

# Frontend
```
cd frontend

python3 -m http.server 5500
```
---

# Docker
```
docker compose up --build
```
---

# Code Style

Please follow:

- clean architecture
- modular design
- descriptive variable names
- simple readable functions

Avoid:
- deeply nested logic
- hardcoded secrets
- unnecessary abstractions

---

# Pull Requests

Before submitting:

- test locally
- verify Docker build
- update README if needed

---

# Branch Naming

Examples:
```
feature/product-search

fix/docker-imports

improvement/langgraph-routing
```
---

# Commit Naming

Examples:
```
feat: add NLP product filtering

fix: resolve docker import issue

docs: improve README
```
---

# Future Contribution Areas

- LangGraph tool calling
- Product recommendations
- PostgreSQL support
- Redis caching
- Authentication
- Streaming responses
- Kubernetes deployment

---

# Security

Never commit:

- API keys
- `.env`
- SQLite databases
- secrets

Always use `.env.example`.
