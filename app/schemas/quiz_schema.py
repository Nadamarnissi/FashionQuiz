from typing import Optional
from pydantic import BaseModel


class QuizCategoryCreate(BaseModel):
    name: str
    description: Optional[str] = None


class QuizCategoryResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

    class Config:
        orm_mode = True


class QuestionCreate(BaseModel):
    category_id: int
    question_text: str
    option_a: str
    option_b: str
    option_c: str
    option_d: str
    correct_answer: str
    explanation: Optional[str] = None
    difficulty: str = "easy"


class QuestionResponse(BaseModel):
    id: int
    category_id: int
    question_text: str
    option_a: str
    option_b: str
    option_c: str
    option_d: str
    correct_answer: str
    explanation: Optional[str] = None
    difficulty: str

    class Config:
        orm_mode = True


class AnswerSubmit(BaseModel):
    question_id: int
    selected_answer: str


class ScoreCreate(BaseModel):
    category_id: int
    score: int
    total_questions: int 