from sqlalchemy import Column, Integer, String, Float, DateTime, Enum
from datetime import datetime
import enum

from app.database.base import Base


class UserRole(str, enum.Enum):
    STUDENT = "student"
    SALARIED = "salaried"
    FREELANCE = "freelance"
    ENTREPRENEUR = "entrepreneur"
    RETIRED = "retired"
    UNEMPLOYED = "unemployed"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    role = Column(Enum(UserRole), default=UserRole.STUDENT)

    monthly_income = Column(Float, default=0)

    created_at = Column(DateTime, default=datetime.utcnow)