from fastapi import APIRouter
from pydantic import BaseModel
import requests
router = APIRouter(
    prefix="/ai",
    tags=["AI Assistant"]
)


@router.get("/feedback/{score}/{total}")
def get_ai_feedback(score: int, total: int):
    percentage = (score / total) * 100 if total > 0 else 0

    if percentage >= 80:
        message = "Excellent fashion sense! You clearly understand luxury brands and fashion culture."
        avatar_mood = "happy"
    elif percentage >= 50:
        message = "Good effort! You have a solid base, but you can improve your fashion knowledge."
        avatar_mood = "neutral"
    else:
        message = "Keep practicing! Fashion history and brand recognition take time to master."
        avatar_mood = "encouraging"

    return {
        "message": message,
        "avatar_mood": avatar_mood,
        "score": score,
        "total": total
    }
class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
def chat_with_ollama(chat_request: ChatRequest):
    print(f"Received chat message: {chat_request.message}")
    response = requests.post(
    "http://127.0.0.1:11434/api/chat",
    json={
        "model": "phi3",
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a fast fashion assistant inside a mobile quiz app. "
                    "Always answer in maximum 2 short sentences. "
                    "Keep answers concise, direct, and lightweight. "
                    "Do not explain too much. "
                    "Focus only on fashion-related topics."
                )
            },
            {
                "role": "user",
                "content": chat_request.message
            }
        ],
        "stream": False
    },
    timeout=120
)

    data = response.json()

    return {
        "answer": data["message"]["content"]
    }