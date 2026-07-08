from pydantic import BaseModel


class AccountCreate(BaseModel):
    name: str
    type: str
    balance: int = 0


class TransactionCreate(BaseModel):
    amount: int
    type: str
    category: str
    description: str = ""
    account_id: int