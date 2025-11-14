from fastapi import APIRouter, HTTPException, status
from uuid import UUID
from ..services.account_event_service import AccountEventService
from ..schemas.account_event import Types

account_event_router = APIRouter(prefix="/account-event")


# not needed as we wanna explicitly have the states in the class
# def get_account_service():
#     return AccountService()

account_event_service = AccountEventService()


@account_event_router.post("/")
def create_account_event(balance: int = 0):
    account = account_event_service.create(balance)
    return {"data": account}


@account_event_router.get("/{account_id}")
def get_account_events(account_id: UUID):
    account_events = account_event_service.get_account_events_by_account_id(account_id)
    return {"data": account_events}


@account_event_router.post("/deposit/{account_id}")
def deposit(account_id: UUID, amount: int):
    account_event_service.deposit_money(amount=amount, account_id=account_id)
    return {"message": "Amount deposited"}


@account_event_router.post("/withdraw/{account_id}")
def withdraw(account_id: UUID, amount: float):
    events = list(
        filter(
            lambda e: e.account_id == account_id, get_account_events(account_id)["data"]
        )
    )
    balance = sum(
        e.amount
        if e.type == Types.DEPOSIT or e.type == Types.CREATE_ACCOUNT
        else -e.amount
        for e in events
    )

    if balance < amount:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "Insufficient balance")

    account_event_service.withdraw(account_id=account_id, amount=amount)
    return {"message": "Amount withdrawn"}


@account_event_router.get("/{account_id}/balance")
def check_balance(account_id: UUID):
    events = list(
        filter(
            lambda e: e.account_id == account_id, get_account_events(account_id)["data"]
        )
    )
    return sum(
        ac.amount
        if ac.type == Types.DEPOSIT or ac.type == Types.CREATE_ACCOUNT
        else -ac.amount
        for ac in events
    )
