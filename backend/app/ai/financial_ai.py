from collections import defaultdict


class FinancialAI:

    def __init__(self):
        pass

    #  Analyse simple des dépenses
    def analyze_transactions(self, transactions):

        summary = defaultdict(int)

        total_income = 0
        total_expense = 0

        for t in transactions:

            if t.type == "income":
                total_income += t.amount
            else:
                total_expense += t.amount
                summary[t.category] += t.amount

        savings = total_income - total_expense

        return {
            "total_income": total_income,
            "total_expense": total_expense,
            "savings": savings,
            "spending_by_category": dict(summary)
        }

    #  Détection dépenses inutiles
    def detect_unnecessary_spending(self, transactions):

        alerts = []

        for t in transactions:

            if t.type == "expense":

                if t.category in ["streaming", "subscriptions", "entertainment"] and t.amount > 50:

                    alerts.append({
                        "type": "warning",
                        "message": f"Dépense élevée sur {t.category}: {t.amount}"
                    })

        return alerts

    #  Score financier (0-1000)
    def financial_score(self, income, expense):

        if income == 0:
            return 0

        ratio = expense / income

        score = 1000 - (ratio * 1000)

        if score < 0:
            score = 0

        return int(score)

    #  prédiction fin de mois simple
    def predict_month_end_balance(self, income, expense, days_passed):

        if days_passed == 0:
            return income

        daily_spend = expense / days_passed

        projected_month_spend = daily_spend * 30

        return income - projected_month_spend