from pydantic import BaseModel


class TransactionRequest(BaseModel):
    source_account_id: int
    destination_account_id: int
    amount: float
