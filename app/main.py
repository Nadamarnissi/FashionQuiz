from fastapi import FastAPI
from app.database import engine, Base
from app.models.user import User
from app.models.quiz import QuizCategory, Question
from app.routes import auth
from app.routes import quiz
from app.models.result import QuizResult
from app.routes import ai

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(quiz.router)
app.include_router(ai.router)
@app.get("/")
def root():
    return {
        "message": "Fashion Quiz AI Backend Running"
    }