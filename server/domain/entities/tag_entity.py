from typing import Optional
from beanie import Document
from datetime import datetime
from enum import Enum

from server.core.types import string


class TagType(Enum):
    Problem = 1
    Blog = 2

    def toInt(self):
        return self.value


class TagEntity(Document):
    name: string
    type: int
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    deleted_at: Optional[datetime] = None

    class Settings:
        name = "tags"

    @staticmethod
    def new(name: string, type: TagType):
        return TagEntity(
            name=name,
            type=type.toInt(),
            created_at=datetime.now(),
            updated_at=datetime.now(),
            deleted_at=None,
        )
