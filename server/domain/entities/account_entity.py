from typing import Optional
from beanie import Document
from pydantic import EmailStr
from datetime import datetime
from enum import Enum

from server.core.types import string

class AccountType(Enum):
    OAuth = 1
    Email = 2

    def toInt(self):
        return self.value

class AccountEntity(Document):
    username: string
    email: EmailStr
    password: string
    account_type: int
    device_token: string
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    deleted_at: Optional[datetime] = None
    
    class Settings:
        name = "accounts"