from enum import Enum
from uuid import UUID, uuid4
from datetime import datetime, timezone

from pydantic import BaseModel


class Types(str, Enum):
    WITHDRAW = "withdraw"
    DEPOSIT = "deposit"
    CREATE_ACCOUNT = "create_account"


class AccountEvent(BaseModel):
    account_id: UUID = uuid4()
    type: Types
    amount: float
    timestamp: datetime = datetime.now(tz=timezone.utc)
