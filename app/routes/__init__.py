from fastapi import APIRouter
from .account import account_router

api_router = APIRouter(prefix="/api")

api_router.include_router(account_router)
