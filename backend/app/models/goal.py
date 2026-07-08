from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from datetime import datetime

from app.database.base import Base


class Goal(Base):
    __tablename__ = "goals"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    title = Column(String)
    target_amount = Column(Float)
    current_amount = Column(Float, default=0)

    target_date = Column(DateTime)

    created_at = Column(DateTime, default=datetime.utcnow)