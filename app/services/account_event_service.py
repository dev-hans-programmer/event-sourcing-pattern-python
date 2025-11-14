from ..schemas.account_event import AccountEvent, Types
from uuid import UUID


class AccountEventService:
    def __init__(self) -> None:
        self.account_events: list[AccountEvent] = []
        self._by_id: dict[UUID, AccountEvent] = {}

    def create(self, amount: float):
        account_event = AccountEvent(type=Types.CREATE_ACCOUNT, amount=amount)
        self.account_events.append(account_event)
        self._by_id[account_event.account_id] = account_event
        return account_event

    def get_account_events(self):
        return self.account_events

    def get_account_events_by_account_id(self, account_id: UUID):
        return list(filter(lambda ac: ac.account_id == account_id, self.account_events))

    def deposit_money(self, account_id: UUID, amount: float):
        event = AccountEvent(account_id=account_id, amount=amount, type=Types.DEPOSIT)
        self.account_events.append(event)
        return True

    def withdraw(self, account_id: UUID, amount: float):
        event = AccountEvent(account_id=account_id, amount=amount, type=Types.WITHDRAW)
        self.account_events.append(event)
        return True
