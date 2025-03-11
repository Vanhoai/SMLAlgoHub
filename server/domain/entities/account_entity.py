from typing import Optional
from beanie import Document
from pydantic import EmailStr
from datetime import datetime
from enum import Enum

from server.core.types import string


class AccountEntity(Document):
    username: string
    email: string
    avatar: string
    device_token: string
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    deleted_at: Optional[datetime] = None

    class Settings:
        name = "accounts"

    @staticmethod
    def new(username: string, email: EmailStr, avatar: string, device_token: string):
        return AccountEntity(
            username=username,
            email=email,
            avatar=avatar,
            device_token=device_token,
            created_at=datetime.now(),
            updated_at=datetime.now(),
            deleted_at=None,
        )
