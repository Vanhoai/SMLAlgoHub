from abc import ABC, abstractmethod
from typing import Optional

from server.domain.entities.course_entity import CourseEntity
from server.core.types import string

class ManageCourseUseCase(ABC):
    @abstractmethod
    async def find(self, id: string) -> Optional[CourseEntity]: ...
