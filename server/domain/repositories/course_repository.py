from server.domain.entities.course_entity import CourseEntity
from server.domain.repositories.base_repository import BaseRepository
from server.database import client

class CourseRepository(BaseRepository[CourseEntity]):
    def __init__(self):
        collection = client.get_collection('courses')
        super().__init__(collection, CourseEntity)
