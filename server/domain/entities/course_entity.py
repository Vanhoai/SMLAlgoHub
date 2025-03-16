from server.core.helpers.time import TimeHelper
from server.core.types import string
from server.domain.entities.base_entity import BaseEntity


class CourseEntity(BaseEntity):
    author: string
    title: string
    total_lessons: int
    total_learned: int
    total_exercises: int

    @staticmethod
    def new(
        author: string,
        title: string,
        total_lessons: int,
        total_learned: int,
        total_exercises: int,
    ):
        return CourseEntity(
            id=None,
            author=author,
            title=title,
            total_lessons=total_lessons,
            total_learned=total_learned,
            total_exercises=total_exercises,
            created_at=TimeHelper.utc_timezone(),
            updated_at=TimeHelper.utc_timezone(),
            deleted_at=None,
        )
