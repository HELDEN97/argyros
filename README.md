# ARGYROS - Assistant intelligent de gestion financière

## Présentation

Argyros est une plateforme SaaS de gestion financière personnelle augmentée par intelligence artificielle. Elle permet de suivre les revenus et dépenses, définir des objectifs financiers, analyser les comportements de consommation et recevoir des recommandations personnalisées.

Le système s’adapte automatiquement au profil utilisateur :
- Étudiant
- Salarié
- Entrepreneur
- Commerçant
- Freelance

---

## Fonctionnalités principales

### Gestion financière
- Suivi des revenus et dépenses
- Gestion de comptes multiples (banque, cash, épargne, crypto)
- Catégorisation automatique des transactions
- Calcul automatique du solde

### Objectifs financiers
- Création d’objectifs (voyage, voiture, études, logement, épargne)
- Suivi de progression
- Définition de montants cibles et d’échéances
- Suivi automatique de l’avancement

### Assistant intelligent (IA)
- Analyse des habitudes financières
- Conseils personnalisés
- Réponses en langage naturel
- Aide à la prise de décision financière
- Prévisions de fin de mois

### Tableau de bord
- Visualisation des revenus et dépenses
- Suivi de l’épargne
- Indicateur de santé financière (score)
- Suivi des objectifs

### Système de score financier
- Score de 0 à 1000
- Basé sur :
  - Taux d’épargne
  - Niveau de dépenses
  - Discipline budgétaire
  - Endettement

### Système d’alertes
- Détection de dépenses anormales
- Détection d’abonnements inutiles
- Alertes de dépassement de budget

### Gamification
- Système de badges
- Progression utilisateur
- Niveau financier

### Export et reporting
- Export de rapports financiers en PDF
- Résumé mensuel automatique

---

## Architecture du projet

```
argyros/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── ai/
│   │   ├── core/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── database/
│   │   └── main.py
│   │
│   ├── requirements.txt
│   ├── .env
│   └── Dockerfile
│
├── frontend/
│   ├── app/
│   ├── lib/
│   ├── components/
│   └── package.json
│
└── docker-compose.yml


```

## Stack technique
 Backend
 Python
 FastAPI
 SQLAlchemy
 PostgreSQL
 JWT Authentication
 OpenAI API
 
## Frontend
 Next.js
 React
 TypeScript
 Tailwind CSS
 
## Intelligence artificielle
 Modèle GPT (OpenAI)
 Analyse contextuelle des finances
 Système de recommandations personnalisées
 
## Infrastructure
 Docker
 API REST
 Architecture modulaire
 
# Installation
##Cloner le projet
git clone https://github.com/your-username/argyros.git
cd argyros

## Backend
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt

Créer un fichier .env :

DATABASE_URL=postgresql://postgres:postgres@localhost:5432/argyros
SECRET_KEY=your_secret_key
OPENAI_API_KEY=your_openai_key

Lancer le backend :

uvicorn app.main:app --reload
