from app.models.notification import Notification


class NotificationService:

    def create_alert(self, user_id: int, title: str, message: str, type="info"):

        return {
            "user_id": user_id,
            "title": title,
            "message": message,
            "type": type
        }

    def auto_notifications(self, transactions):

        notifications = []

        total_expense = sum(
            t.amount for t in transactions if t.type == "expense"
        )

        if total_expense > 2000:

            notifications.append({
                "title": "Budget dépassé",
                "message": "Tes dépenses sont élevées ce mois-ci",
                "type": "warning"
            })

        return notifications