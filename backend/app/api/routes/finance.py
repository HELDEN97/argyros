from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.database.base import get_db
from app.core.deps import get_current_user

from app.schemas.finance import AccountCreate, TransactionCreate
from app.services.finance_service import (
    create_account,
    get_accounts,
    create_transaction,
    get_transactions
)

router = APIRouter(prefix="/finance", tags=["Finance"])


# ACCOUNTS

@router.post("/accounts")
def add_account(
    payload: AccountCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return create_account(db, user.id, payload)


@router.get("/accounts")
def list_accounts(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return get_accounts(db, user.id)


# TRANSACTIONS

@router.post("/transactions")
def add_transaction(
    payload: TransactionCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return create_transaction(db, user.id, payload)


@router.get("/transactions")
def list_transactions(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return get_transactions(db, user.id)