from enum import Enum
from server.core.helpers.time import TimeHelper
from server.domain.entities.base_entity import BaseEntity
from server.core.types import string
from typing import List

class BlogStatus(Enum):
    CREATED = 1
    PUBLISHED = 2
    DELETED = 3

    def to_value(self):
        return self.value

class BlogEntity(BaseEntity):
    author_id: string
    thumbnail_url: string
    title: string
    content: string
    count_favourite: int
    status: int
    tags: List[string]

    @staticmethod
    def new(
        author_id: string,
        thumbnail_url: string,
        title: string,
        content: string,
        count_favourite: int,
        tags: List[string] = [],
        status: BlogStatus = BlogStatus.CREATED):
        return BlogEntity(
            id=None,
            author_id=author_id,
            thumbnail_url=thumbnail_url,
            title=title,
            content=content,
            count_favourite=count_favourite,
            status=status.to_value(),
            tags=tags,
            created_at=TimeHelper.utc_timezone(),
            updated_at=TimeHelper.utc_timezone(),
            deleted_at=None
        )
