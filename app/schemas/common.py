from pydantic import BaseModel
from datetime import datetime, timezone


class Mixin(BaseModel):
    timestamp: datetime = datetime.now(tz=timezone.utc)
