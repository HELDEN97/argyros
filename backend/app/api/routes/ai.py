from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.core.deps import get_current_user
from app.models.transaction import Transaction
from app.services.ai_service import AIService

router = APIRouter(prefix="/ai", tags=["AI"])


@router.get("/intelligence")
def intelligence(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):

    transactions = db.query(Transaction).filter(
        Transaction.user_id == user.id
    ).all()

    service = AIService()

    return service.full_intelligence(db, user.id, transactions)