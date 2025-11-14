from .common import Mixin
from uuid import UUID


class AccountIn(Mixin):
    account_id: UUID
    balance: float = 0


class Account(AccountIn):
    id: int
