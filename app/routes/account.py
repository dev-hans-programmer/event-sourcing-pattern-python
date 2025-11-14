from fastapi import APIRouter, HTTPException, status
from uuid import UUID
from ..services.account_service import AccountService

account_router = APIRouter(prefix="/account")


# not needed as we wanna explicitly have the states in the class
# def get_account_service():
#     return AccountService()

account_service = AccountService()


@account_router.post("/")
def create_account(balance: int = 0):
    account = account_service.create(balance)
    return {"data": account}


@account_router.get("/")
def get_accounts():
    accounts = account_service.get_accounts()
    return {"data": accounts}


@account_router.post("/deposit/{account_id}")
def deposit(account_id: UUID, amount: int):
    account = account_service.get_account(account_id)
    if not account:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "Account not found")

    account.balance += amount
    return {"message": "Amount deposited", "current_balance": account.balance}


@account_router.post("/withdraw/{account_id}")
def withdraw(account_id: UUID, amount: int):
    account = account_service.get_account(account_id)
    if not account:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "Account not found")

    if account.balance < amount:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "Insufficient balance")
    account.balance -= amount
    return {"message": "Amount withdrawn", "current_balance": account.balance}
