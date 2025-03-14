from typing import Optional
from datetime import datetime
from pydantic import BaseModel
from server.core.types import string


class CourseEntity(BaseModel):
    author: string
    title: string
    total_lessons: int
    total_learned: int
    total_exercises: int
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    deleted_at: Optional[datetime] = None

    @staticmethod
    def new(
        author: string,
        title: string,
        total_lessons: int,
        total_learned: int,
        total_exercises: int,
    ):
        return CourseEntity(
            author=author,
            title=title,
            total_lessons=total_lessons,
            total_learned=total_learned,
            total_exercises=total_exercises
        )
