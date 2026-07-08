from app.ai.financial_ai import FinancialAI
from app.services.alert_service import AlertService
from app.services.score_service import ScoreService
from app.services.gamification_service import GamificationService


class AIService:

    def full_intelligence(self, db, user_id, transactions):

        ai = FinancialAI()

        alert_service = AlertService()
        score_service = ScoreService()
        gamification = GamificationService()

        analysis = ai.analyze_transactions(transactions)

        alerts = alert_service.detect_anomalies(transactions)

        score = score_service.calculate_score(db, user_id)

        badges = gamification.generate_badges(user_id, score)

        return {
            "analysis": analysis,
            "alerts": alerts,
            "score": score,
            "badges": badges
        }