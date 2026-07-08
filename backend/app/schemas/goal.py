from pydantic import BaseModel
from datetime import datetime


class GoalCreate(BaseModel):
    title: str
    target_amount: int
    category: str
    deadline: datetime | None = None