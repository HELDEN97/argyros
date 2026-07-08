from sqlalchemy.orm import Session

from app.models.transaction import Transaction
from app.models.goal import Goal


class DashboardService:

    def get_dashboard(self, db: Session, user_id: int):

        transactions = db.query(Transaction).filter(
            Transaction.user_id == user_id
        ).all()

        goals = db.query(Goal).filter(
            Goal.user_id == user_id
        ).all()

        total_income = sum(t.amount for t in transactions if t.type == "income")
        total_expense = sum(t.amount for t in transactions if t.type == "expense")

        savings = total_income - total_expense

        goals_progress = []

        for g in goals:

            progress = 0

            if g.target_amount > 0:
                progress = (g.current_amount / g.target_amount) * 100

            goals_progress.append({
                "title": g.title,
                "category": g.category,
                "progress": round(progress, 2),
                "target": g.target_amount,
                "current": g.current_amount
            })

        return {
            "finance": {
                "income": total_income,
                "expense": total_expense,
                "savings": savings
            },
            "goals": goals_progress
        }