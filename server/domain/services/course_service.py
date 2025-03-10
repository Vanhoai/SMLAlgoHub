from server.domain.usecases.course_usecases import ManageCourseUseCase
from server.core.types import string
from server.domain.entities.course_entity import CourseEntity


class CourseService(ManageCourseUseCase):
    def sign_in(self, id: string) -> CourseEntity:
        pass
