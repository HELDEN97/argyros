from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware #ressoudre pb cross

from app.core.config import settings
from app.api.routes.auth import router as auth_router
from app.api.routes.finance import router as finance_router

from app.api.routes.goals import router as goals_router
from app.api.routes.dashboard import router as dashboard_router

from app.api.routes.ai import router as ai_router

#from app.database import Base, engine

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(finance_router)
app.include_router(ai_router)
app.include_router(goals_router)
app.include_router(dashboard_router)

@app.get("/")
def root():
    return {"status": "Argyros API running"}


@app.get("/health")
def health():
    return {"status": "ok"}
