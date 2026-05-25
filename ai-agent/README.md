# LangGraph AI Agent

AI Agent for conversational product search.

Uses:
- LangGraph
- Gemini AI
- FastAPI

---

# Architecture
```
Frontend
    ↓
AI Agent
    ↓
FastAPI Product APIs
```
---

# Features

- Conversational Product Search
- Product Filtering
- Gemini AI Integration
- LangGraph Workflow
- Structured Product Responses

---

# Setup

Create virtual environment:
```
python3 -m venv venv
```
Activate:

Mac/Linux:
```
source venv/bin/activate
```

Windows:
```
venv\Scripts\activate
```
---

# Install Dependencies
```
pip install fastapi uvicorn langgraph langchain requests python-dotenv langchain-google-genai
```
---

# Environment Variables

Create `.env`

```
GOOGLE_API_KEY=your_key
PRODUCT_API=http://127.0.0.1:8000/api/v1
```
---

# Run AI Agent
```
uvicorn main:api --reload --port 9000
```

Runs on:
http://127.0.0.1:9000

Swagger:
http://127.0.0.1:9000/docs

---

# Example Request

```
POST /chat
```

```
{
  "message": "products under 1000"
}
```

---

# Example Response
```
{
  "products": [
    {
      "id": 1,
      "name": "Laptop",
      "price": 999
    }
  ]
}
```
---

# Folder Structure
```
ai-agent/
│
├── graph/
├── tools/
├── main.py
└── .env
```
---

# Future Improvements

- Real Tool Calling
- Multi-Agent Architecture
- Memory
- Recommendation Engine
- Semantic Search
- Vector Database
- MCP Integration
- Autonomous Workflows