from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Enum, Boolean
from datetime import datetime
import enum

from app.database.base import Base


class TransactionType(str, enum.Enum):
    INCOME = "income"
    EXPENSE = "expense"


class AccountType(str, enum.Enum):
    CASH = "cash"
    BANK = "bank"
    SAVINGS = "savings"


class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    name = Column(String)
    type = Column(Enum(AccountType))
    balance = Column(Float, default=0)


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    type = Column(Enum(TransactionType))
    category = Column(String)
    label = Column(String)
    amount = Column(Float)

    date = Column(DateTime, default=datetime.utcnow)


class Budget(Base):
    __tablename__ = "budgets"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    category = Column(String)
    limit_amount = Column(Float)