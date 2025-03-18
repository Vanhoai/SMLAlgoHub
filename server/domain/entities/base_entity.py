from datetime import datetime
from typing import Optional

from server.core.types import string
from fastapi_camelcase import CamelModel

class BaseEntity(CamelModel):
    id: Optional[string] = None
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    deleted_at: Optional[datetime] = None
