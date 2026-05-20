from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.user import User
from app.models.result import QuizResult
from app.routes.auth import get_current_user
from app.database import SessionLocal
from app.models.quiz import QuizCategory, Question

from app.schemas.quiz_schema import (
    QuizCategoryCreate,
    QuizCategoryResponse,
    QuestionCreate,
    QuestionResponse,
    AnswerSubmit,
    ScoreCreate
)

router = APIRouter(
    prefix="/quiz",
    tags=["Quiz"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/categories")
def create_category(
    category_data: QuizCategoryCreate,
    db: Session = Depends(get_db)
):
    category = QuizCategory(
        name=category_data.name,
        description=category_data.description
    )

    db.add(category)
    db.commit()
    db.refresh(category)

    return category

@router.get("/categories")
def get_categories(
    db: Session = Depends(get_db)
):
    
    categories = db.query(QuizCategory).all()

    return categories
@router.post("/questions")
def create_question(
    question_data: QuestionCreate,
    db: Session = Depends(get_db)
):
    question = Question(
        category_id=question_data.category_id,
        question_text=question_data.question_text,
        option_a=question_data.option_a,
        option_b=question_data.option_b,
        option_c=question_data.option_c,
        option_d=question_data.option_d,
        correct_answer=question_data.correct_answer,
        explanation=question_data.explanation,
        difficulty=question_data.difficulty
    )

    db.add(question)
    db.commit()
    db.refresh(question)

    return question


@router.get("/questions")
def get_questions(
    db: Session = Depends(get_db)
):
    questions = db.query(Question).all()
    return questions

@router.get("/start/{category_id}")
def start_quiz(
    category_id: int,
    db: Session = Depends(get_db)
):
    questions = db.query(Question).filter(
        Question.category_id == category_id
    ).all()

    return {
        "category_id": category_id,
        "total_questions": len(questions),
        "questions": questions
    }

@router.post("/answer")
def submit_answer(
    answer_data: AnswerSubmit,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    question = db.query(Question).filter(
        Question.id == answer_data.question_id
    ).first()

    if not question:
        return {
            "error": "Question not found"
        }

    is_correct = answer_data.selected_answer.upper() == question.correct_answer.upper()
    
    result = QuizResult(
        user_id=current_user.id,
        question_id=question.id,
        selected_answer=answer_data.selected_answer.upper(),
        is_correct=is_correct
    )

    db.add(result)
    db.commit()

    return {
        "question_id": question.id,
        "selected_answer": answer_data.selected_answer.upper(),
        "correct_answer": question.correct_answer.upper(),
        "is_correct": is_correct,
        "explanation": question.explanation
    }
@router.post("/score")
def save_score(
    score_data: ScoreCreate,
    db: Session = Depends(get_db)
):
    result = QuizResult(
        user_id=1,
        category_id=score_data.category_id,
        score=score_data.score,
        total_questions=score_data.total_questions
    )

    db.add(result)
    db.commit()
    db.refresh(result)

    return {
        "message": "Score saved successfully",
        "id": result.id,
        "score": result.score,
        "total_questions": result.total_questions
    }
@router.get("/scores")
def get_scores(
    db: Session = Depends(get_db)
):
    results = db.query(QuizResult, QuizCategory).join(
        QuizCategory,
        QuizResult.category_id == QuizCategory.id
    ).all()

    return [
        {
            "category_name": category.name,
            "score": result.score,
            "total_questions": result.total_questions
        }
        for result, category in results
    ]