from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from server.core.types import string

class BaseEntity(BaseModel):
    id: Optional[string] = None
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    deleted_at: Optional[datetime] = None
