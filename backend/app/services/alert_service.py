from app.models.transaction import Transaction


class AlertService:

    def detect_anomalies(self, transactions):

        alerts = []

        for t in transactions:

            if t.type == "expense":

                if t.amount > 500:
                    alerts.append({
                        "type": "warning",
                        "message": f"Dépense élevée détectée : {t.amount}€ ({t.category})"
                    })

                if t.category == "gambling":
                    alerts.append({
                        "type": "critical",
                        "message": "Dépense à risque détectée (gambling)"
                    })

        return alerts