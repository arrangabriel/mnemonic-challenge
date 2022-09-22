from pydantic import BaseModel


class Account(BaseModel):
    id: int
    name: str
    balance: float


class Transaction(BaseModel):
    id: int
    registered_time: int # Epoch milliseconds
    executedTime: int    # Epoch milliseconds
    success: bool
    amount: float
    source_account: Account
    destination_account: Account