from fastapi import APIRouter
from pydantic import BaseModel
import ollama

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/")
def chat(req: ChatRequest):

    prompt = f"""
Tu es SeniorCare AI, un assistant médical pour personnes âgées.
Réponds de façon claire, rassurante et simple.

Question du patient :
{req.message}
"""

    response = ollama.chat(
        model="llama3",
        messages=[
            {"role": "system", "content": "Tu es un assistant médical pour seniors."},
            {"role": "user", "content": req.message}
        ]
    )

    reply = response["message"]["content"]

    return {
        "response": reply
    }
