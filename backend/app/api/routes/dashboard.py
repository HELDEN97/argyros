from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.database.base import get_db
from app.core.deps import get_current_user

from app.services.dashboard_service import DashboardService

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


@router.get("/")
def get_dashboard(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):

    service = DashboardService()

    return service.get_dashboard(db, user.id)