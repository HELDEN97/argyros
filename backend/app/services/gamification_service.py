from app.models.badge import Badge


class GamificationService:

    def generate_badges(self, user_id: int, score: int):

        badges = []

        if score > 800:
            badges.append({
                "name": "Master Saver",
                "description": "Excellent gestion financière",
                "icon": "star"
            })

        elif score > 500:
            badges.append({
                "name": "Good Manager",
                "description": "Bonne gestion des finances",
                "icon": "medal"
            })

        else:
            badges.append({
                "name": "Starter",
                "description": "Début dans la gestion financière",
                "icon": "leaf"
            })

        return badges