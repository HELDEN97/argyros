from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.core.deps import get_current_user

from app.schemas.goal import GoalCreate
from app.services.goal_service import (
    create_goal,
    get_goals,
    update_goal_progress
)

router = APIRouter(prefix="/goals", tags=["Goals"])


@router.post("/")
def add_goal(
    payload: GoalCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return create_goal(db, user.id, payload)


@router.get("/")
def list_goals(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return get_goals(db, user.id)


@router.put("/{goal_id}/progress")
def progress_goal(
    goal_id: int,
    amount: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return update_goal_progress(db, goal_id, amount)