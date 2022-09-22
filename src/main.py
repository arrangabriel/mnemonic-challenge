from fastapi import FastAPI
import uvicorn

from core.backend import Backend
from models import Account, TransactionRequest

api = FastAPI()

backend = Backend()


@api.get("/accounts", response_model=list[Account])
def get_accounts():
    return backend.accounts


@api.get("/accounts/{account_id}")
def get_account(account_id: int):
    try:
        return backend.get_account(account_id)
    except ValueError as e:
        return {"error": str(e)}


@api.post("/transaction")
def create_transaction(transaction_request: TransactionRequest):
    pass


def main():
    uvicorn.run("main:api", port=8000, reload=True)


if __name__ == "__main__":
    main()
