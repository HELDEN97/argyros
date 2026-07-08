# Argyros

<p align="center">
  <img src="docs/assets/logo.png" alt="Logo Argyros" width="180">
</p>

<h3 align="center">
Pilotez vos finances. Préparez votre avenir.
</h3>

<p align="center">
Une plateforme moderne de gestion financière personnelle développée avec Python, FastAPI et React.
</p>

---

# À propos

**Argyros** est une plateforme de **gestion financière personnelle (Personal Finance Management - PFM)** permettant à chacun de centraliser, organiser, analyser et planifier ses finances.

L'objectif d'Argyros est de fournir une vision claire et globale de la situation financière de l'utilisateur afin de l'aider à prendre de meilleures décisions.

Contrairement aux applications bancaires, **Argyros ne se connecte jamais à une banque**, ne réalise aucun paiement et ne détient aucun fonds.

L'utilisateur reste entièrement propriétaire de ses données financières.

---

# Vision du projet

Argyros est conçu pour devenir un véritable **assistant de pilotage financier**.

Il permet notamment de :

* suivre ses revenus et ses dépenses ;
* organiser ses comptes financiers ;
* gérer son patrimoine ;
* suivre ses investissements ;
* construire et suivre des budgets ;
* préparer des projets financiers ;
* visualiser l'évolution de sa situation financière ;
* prendre des décisions grâce à des indicateurs et des analyses.

---

# Ce qu'Argyros n'est pas

Argyros **n'est pas** :

* une banque ;
* un établissement de paiement ;
* un logiciel de comptabilité ;
* un agrégateur bancaire (Open Banking / DSP2) ;
* une plateforme de trading ;
* un gestionnaire de portefeuille sous mandat.

Argyros est un **outil de gestion et d'analyse des informations financières personnelles**.

---

# Fonctionnalités principales

## Tableau de bord

* Vue globale des finances
* Patrimoine net
* Cash-flow
* Revenus et dépenses
* Budgets
* Objectifs financiers
* Graphiques interactifs
* Indicateurs clés

---

## Gestion des comptes

Création de comptes personnalisés :

* Compte courant
* Livret d'épargne
* Espèces
* Portefeuille crypto
* Compte titres
* PEA
* Compte professionnel
* Comptes personnalisés

Chaque compte est entièrement géré par l'utilisateur.

---

## Transactions

Gestion des :

* Revenus
* Dépenses
* Virements internes
* Transactions récurrentes

Fonctionnalités :

* Catégories
* Sous-catégories
* Tags
* Pièces jointes
* Recherche avancée
* Filtres

---

## Budgets

* Budgets mensuels
* Budgets annuels
* Budgets par catégorie
* Alertes de dépassement
* Comparaison prévisionnel / réel

---

## Patrimoine

Suivi de tous les actifs :

* Comptes
* Immobilier
* Investissements
* Crypto-actifs
* Véhicules
* Objets de valeur

Suivi des passifs :

* Emprunts
* Crédits
* Dettes

Calcul automatique du patrimoine net.

---

## Investissements

Suivi des :

* Actions
* ETF
* Obligations
* SCPI
* Fonds
* Crypto-actifs
* Métaux précieux

Argyros permet uniquement le **suivi des investissements**.

Aucun achat ou vente n'est réalisé depuis l'application.

---

## Immobilier

Gestion des biens immobiliers :

* Valeur d'acquisition
* Valeur estimée
* Revenus locatifs
* Charges
* Rentabilité
* Crédit associé

---

## Emprunts

Suivi :

* Capital restant
* Intérêts
* Échéancier
* Mensualités

---

## Objectifs financiers

Création et suivi d'objectifs :

* Achat immobilier
* Voyage
* Véhicule
* Fonds d'urgence
* Retraite
* Études

---

## Calendrier financier

Visualisation :

* Paiements récurrents
* Échéances
* Abonnements
* Crédits
* Rappels financiers

---

## Documents

Classement sécurisé :

* Factures
* Contrats
* Garanties
* Assurances
* Documents administratifs

---

## Rapports

Export :

* PDF
* Excel

Statistiques :

* Revenus
* Dépenses
* Patrimoine
* Budgets
* Investissements

---

## Assistant IA *(Prévu)*

Les futures versions intégreront un assistant intelligent capable de :

* analyser les habitudes financières ;
* proposer des optimisations budgétaires ;
* anticiper les dépenses ;
* générer automatiquement des rapports ;
* répondre aux questions de l'utilisateur.

---

# Technologies

## Backend

* Python 3.13
* FastAPI
* SQLAlchemy 2.x
* Alembic
* PostgreSQL
* Redis
* Celery
* Pydantic

---

## Frontend

* React
* TypeScript
* Vite
* Tailwind CSS
* shadcn/ui
* TanStack Query
* React Router

---

## Infrastructure

* Docker
* Docker Compose
* GitHub Actions
* Nginx
* Sentry
* Prometheus
* Grafana

---

# Architecture du projet

```
argyros/

├── backend/
│   ├── app/
│   ├── tests/
│   ├── migrations/
│   └── requirements/
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── tests/
│
├── docs/
├── scripts/
├── docker/
├── .github/
│
├── README.md
├── LICENSE
└── docker-compose.yml
```

---

# Installation

## Cloner le projet

```bash
git clone https://github.com/votre-utilisateur/argyros.git

cd argyros
```

---

## Installation du Backend

Créer un environnement virtuel :

```bash
python -m venv .venv
```

Activation :

Linux / macOS

```bash
source .venv/bin/activate
```

Windows

```powershell
.venv\Scripts\activate
```

Installer les dépendances :

```bash
pip install -r requirements.txt
```

---

## Installation du Frontend

```bash
npm install
```

---

# Variables d'environnement

Backend

```
DATABASE_URL=

SECRET_KEY=

REDIS_URL=

ENVIRONMENT=

ACCESS_TOKEN_EXPIRE_MINUTES=

SENTRY_DSN=
```

Frontend

```
VITE_API_URL=
```

---

# Base de données

Créer une migration

```bash
alembic revision --autogenerate
```

Appliquer les migrations

```bash
alembic upgrade head
```

---

# Lancer l'application

Backend

```bash
uvicorn app.main:app --reload
```

Frontend

```bash
npm run dev
```

---

# Tests

Backend

```bash
pytest
```

Couverture de tests

```bash
pytest --cov=app
```

Frontend

```bash
npm run test
```

---

# Qualité du code

Python

```bash
ruff check

ruff format

mypy
```

Frontend

```bash
npm run lint

npm run format
```

---

# Documentation de l'API

Une fois le backend lancé :

Swagger

```
/docs
```

ReDoc

```
/redoc
```

---

# Sécurité

Argyros met en œuvre :

* Authentification JWT
* Hachage sécurisé des mots de passe
* Jetons de rafraîchissement
* Gestion des rôles et permissions
* Chiffrement des données sensibles
* Protection contre les injections SQL
* Protection XSS
* Gestion sécurisée des sessions
* Configuration HTTPS

---

# Feuille de route

## MVP

* Authentification
* Tableau de bord
* Comptes
* Transactions
* Catégories
* Budgets
* Rapports
* Import CSV

---

## Version 2

* Gestion du patrimoine
* Investissements
* Immobilier
* Emprunts
* Calendrier financier
* Documents

---

## Version 3

* Assistant IA
* Prévisions financières
* Simulations
* Application mobile
* API publique

---

# Documentation

La documentation technique et fonctionnelle est disponible dans le dossier **/docs**.

Elle comprend :

* Vision produit
* Cahier des charges
* Cahier fonctionnel
* Architecture technique
* Modèle de données
* Documentation API
* Guide de déploiement

---

# Contribution

Les contributions sont les bienvenues.

Processus recommandé :

1. Créer une branche dédiée.
2. Développer la fonctionnalité.
3. Ajouter les tests nécessaires.
4. Ouvrir une Pull Request.
5. Effectuer la revue de code avant fusion.

---

# Licence

Ce projet est distribué sous licence **MIT**.

---

# Auteur

**Helden Merveil Silaho**

Fondateur et développeur du projet **Argyros**.

Une plateforme moderne de gestion financière pensée pour offrir une vision claire, durable et indépendante de vos finances.
