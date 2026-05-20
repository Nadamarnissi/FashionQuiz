from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.sql import func

from app.database import Base


class QuizResult(Base):
    __tablename__ = "quiz_results"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("quiz_categories.id"), nullable=False)

    score = Column(Integer, nullable=False)
    total_questions = Column(Integer, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())