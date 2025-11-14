from ..schemas.account import Account
from uuid import uuid4, UUID


class AccountService:
    def __init__(self) -> None:
        self.accounts: list[Account] = []
        self._by_id: dict[UUID, Account] = {}

    def create(self, balance: int):
        account = Account(
            id=len(self.accounts) + 1, account_id=uuid4(), balance=balance
        )
        self.accounts.append(account)
        self._by_id[account.account_id] = account
        return account

    def get_accounts(self):
        return self.accounts

    def get_account(self, account_id: UUID):
        return self._by_id.get(account_id)
