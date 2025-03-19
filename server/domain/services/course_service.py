from fastapi import Depends
from typing import Optional

from server.domain.repositories.course_repository import CourseRepository
from server.domain.usecases.course_usecases import ManageCourseUseCase
from server.core.types import string
from server.domain.entities.course_entity import CourseEntity

class CourseService(ManageCourseUseCase):
    def __init__(self, course_repository: CourseRepository = Depends()):
        self.course_repository = course_repository

    async def find(self, id: string) -> Optional[CourseEntity]:
        return await self.course_repository.find_one({ "_id": id })
