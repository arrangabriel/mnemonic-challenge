from time import time
from models import Account, Transaction, TransactionRequest
import json

DATA_DIR = "src/data/"


class Backend:
    def __init__(self):
        self.accounts: list[Account] = self.read_accounts()
        self.transactions: list[Transaction] = self.read_transactions()

    def get_account(self, account_id: int) -> Account:
        for account in self.accounts:
            if account.id == account_id:
                return account
        raise ValueError(f"Account with id {account_id} not found")

    def run_transaction(self, request: TransactionRequest) -> Transaction:
        time_start = time() * 1000

        try:
            src_account = self.get_account(request.source_account_id)
            dst_account = self.get_account(request.destination_account_id)
        except ValueError as e:
            # Possibly add granularity to this
            raise e

        error: Exception = None
        if src_account.balance < request.amount:
            error = ValueError(
                f"Account with id: {request.source_account_id} has insufficient funds to complete the transaction")
        else:
            src_account.balance -= request.amount
            dst_account.balance += request.amount
            self.write_accounts()

        time_end = time() * 1000

        transaction = Transaction(
            id=len(self.transactions),
            time_registered=time_start,
            time_executed=time_end,
            success=error is None,
            amount=request.amount,
            source_account=src_account,
            destination_account=dst_account,
        )

        self.transactions.append(transaction)
        self.write_transactions()

        if error is not None:
            raise error

        return transaction

    def read_accounts(self) -> list[Account]:
        with open(f"{DATA_DIR}accounts.json", "r") as f:
            accounts_json = json.load(f)
        return [Account(**account) for account in accounts_json]

    def write_accounts(self) -> None:
        json_accounts = [account.dict() for account in self.accounts]
        with open(f"{DATA_DIR}accounts.json", "w") as f:
            json.dump(json_accounts, f)

    def read_transactions(self) -> list[Transaction]:
        with open(f"{DATA_DIR}transactions.json", "r") as f:
            transactions_json = json.load(f)
        return [Transaction(**transaction) for transaction in transactions_json]

    def write_transactions(self) -> None:
        json_transactions = [transaction.dict()
                             for transaction in self.transactions]
        with open(f"{DATA_DIR}transactions.json", "w") as f:
            json.dump(json_transactions, f)
