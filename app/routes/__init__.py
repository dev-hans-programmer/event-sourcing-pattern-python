from fastapi import APIRouter
from .account import account_router
from .account_event import account_event_router

api_router = APIRouter(prefix="/api")

api_router.include_router(account_router)
api_router.include_router(account_event_router)
