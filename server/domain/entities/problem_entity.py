from enum import Enum
from typing import List

from server.core.helpers.time import TimeHelper
from server.domain.entities.base_entity import BaseEntity
from server.core.types import string

class ProblemLevel(Enum):
    BEGINNER = 1
    EASY = 2
    MEDIUM = 3
    HARD = 4

class IOMode(Enum):
    STANDARD_IO = "Standard IO"
    FILE_IO = "File IO"

class ProblemEntity(BaseEntity):
    author_id: string
    title: string
    description: string
    input: string
    output: string
    note: string
    source: string
    time_limit: int
    memory_limit: int
    io_mode: string
    tags: List[string]
    level: int
    acceptance: float
    sample_input: string
    sample_output: string
    real_input: string
    real_output: string

    @staticmethod
    def new(
        author_id: string,
        title: string,
        description: string,
        input: string,
        output: string,
        source: string,
        time_limit: int,
        memory_limit: int,
        sample_input: string,
        sample_output: string,
        real_input: string,
        real_output: string,
        note: string = "",
        tags: List[string] = [],
        io_mode: IOMode = IOMode.STANDARD_IO,
        level: ProblemLevel = ProblemLevel.BEGINNER
    ):
        return ProblemEntity(
            id=None,
            author_id=author_id,
            title=title,
            description=description,
            input=input,
            output=output,
            note=note,
            source=source,
            time_limit=time_limit,
            memory_limit=memory_limit,
            io_mode=io_mode.value,
            tags=tags,
            level=level.value,
            acceptance=0.0,
            sample_input=sample_input,
            sample_output=sample_output,
            real_input=real_input,
            real_output=real_output,
            created_at=TimeHelper.utc_timezone(),
            updated_at=TimeHelper.utc_timezone(),
            deleted_at=None
        )
