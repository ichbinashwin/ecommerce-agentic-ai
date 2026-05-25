from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from graph.workflow import app as agent


api = FastAPI()

# CORS CONFIGURATION
api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str


@api.post("/chat")
async def chat(req: ChatRequest):

    result = agent.invoke({
        "user_input": req.message
    })

    return {
        "products": result["products"]
    }