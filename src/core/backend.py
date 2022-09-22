from models import Account, Transaction
import json

DATA_DIR = "src/data/"


class Backend:
    def __init__(self):
        self.accounts: list[Account] = self.read_accounts()
        self.transactions: list[Transaction] = []

    def read_accounts(self) -> list[Account]:
        with open(f"{DATA_DIR}accounts.json", "r") as f:
            accounts_json = json.load(f)
        return [Account(**account) for account in accounts_json]

    def get_account(self, account_id: int) -> Account:
        for account in self.accounts:
            if account.id == account_id:
                return account
        raise ValueError(f"Account with id {account_id} not found")
