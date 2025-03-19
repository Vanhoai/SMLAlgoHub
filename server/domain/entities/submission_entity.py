from server.domain.entities.base_entity import BaseEntity
from server.core.types import string

class SubmissionEntity(BaseEntity):
    source_code: string
    language: string
    memory_limit: int
    time_limit: int
    status: int
