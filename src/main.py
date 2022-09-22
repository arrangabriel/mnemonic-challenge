from fastapi import FastAPI, HTTPException
import uvicorn

from core import Backend
from models import Account, TransactionRequest, Transaction

api = FastAPI()

backend = Backend()


@api.get("/accounts", response_model=list[Account])
def get_accounts():
    return backend.accounts


@api.get("/accounts/{account_id}", response_model=Account)
def get_account(account_id: int):
    try:
        return backend.get_account(account_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@api.post("/run_transaction", response_model=Transaction)
def create_transaction(transaction_request: TransactionRequest):
    try:
        return backend.run_transaction(transaction_request)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@api.get("/test")
def test():
    try:
        return backend.run_transaction(TransactionRequest(
            source_account_id=1,
            destination_account_id=2,
            amount=20,
        ))
    except ValueError as e:
        return {"error": str(e)}


if __name__ == "__main__":
    uvicorn.run("main:api", port=8000, reload=True)
