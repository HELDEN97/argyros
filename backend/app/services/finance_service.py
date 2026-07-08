from sqlalchemy.orm import Session

from app.models.account import Account
from app.models.transaction import Transaction


# ACCOUNTS

def create_account(db: Session, user_id: int, data):

    account = Account(
        name=data.name,
        type=data.type,
        balance=data.balance,
        user_id=user_id
    )

    db.add(account)
    db.commit()
    db.refresh(account)

    return account


def get_accounts(db: Session, user_id: int):

    return db.query(Account).filter(Account.user_id == user_id).all()


# TRANSACTIONS

def create_transaction(db: Session, user_id: int, data):

    account = db.query(Account).filter(Account.id == data.account_id).first()

    if not account:
        return None

    transaction = Transaction(
        amount=data.amount,
        type=data.type,
        category=data.category,
        description=data.description,
        account_id=data.account_id,
        user_id=user_id
    )

    # update balance
    if data.type == "income":
        account.balance += data.amount
    else:
        account.balance -= data.amount

    db.add(transaction)
    db.commit()
    db.refresh(transaction)

    return transaction


def get_transactions(db: Session, user_id: int):

    return db.query(Transaction).filter(Transaction.user_id == user_id).all()