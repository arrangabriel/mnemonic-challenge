from pydantic import BaseModel


class Account(BaseModel):
    id: int
    name: str
    balance: float


class Transaction(BaseModel):
    id: int
    time_registered: int  # Epoch milliseconds
    time_executed: int    # Epoch milliseconds
    success: bool
    amount: float
    source_account: Account
    destination_account: Account
