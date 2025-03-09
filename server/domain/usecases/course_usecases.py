from abc import ABC, abstractmethod

from server.domain.entities.course_entity import CourseEntity
from server.core.types import string

class ManageCourseUseCase(ABC):
    @abstractmethod
    def sign_in(self, id: string) -> CourseEntity:
        pass
    