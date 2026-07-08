from sqlalchemy.orm import Session
from app.models.transaction import Transaction


class ScoreService:

    def calculate_score(self, db: Session, user_id: int):

        transactions = db.query(Transaction).filter(
            Transaction.user_id == user_id
        ).all()

        income = sum(t.amount for t in transactions if t.type == "income")
        expense = sum(t.amount for t in transactions if t.type == "expense")

        if income == 0:
            return 0

        savings_rate = (income - expense) / income

        score = savings_rate * 1000

        # pénalité si dépenses trop élevées
        if expense > income:
            score -= 200

        if score < 0:
            score = 0

        if score > 1000:
            score = 1000

        return int(score)