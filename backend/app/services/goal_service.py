from sqlalchemy.orm import Session
from app.models.goal import Goal


def create_goal(db: Session, user_id: int, data):

    goal = Goal(
        title=data.title,
        target_amount=data.target_amount,
        category=data.category,
        deadline=data.deadline,
        user_id=user_id
    )

    db.add(goal)
    db.commit()
    db.refresh(goal)

    return goal


def get_goals(db: Session, user_id: int):

    return db.query(Goal).filter(Goal.user_id == user_id).all()


def update_goal_progress(db: Session, goal_id: int, amount: int):

    goal = db.query(Goal).filter(Goal.id == goal_id).first()

    if not goal:
        return None

    goal.current_amount += amount

    db.commit()
    db.refresh(goal)

    return goal