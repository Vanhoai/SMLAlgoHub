from datetime import datetime

from server.core.types import string
from server.domain.entities.base_entity import BaseEntity

class TagEntity(BaseEntity):
    name: string

    @staticmethod
    def new(name: string):
        return TagEntity(
            id=None,
            name=name,
            created_at=datetime.now(),
            updated_at=datetime.now(),
            deleted_at=None
        )
