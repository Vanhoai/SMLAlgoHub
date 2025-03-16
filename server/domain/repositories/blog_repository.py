from server.database import client
from server.domain.entities.blog_entity import BlogEntity
from server.domain.repositories.base_repository import BaseRepository

class BlogRepository(BaseRepository[BlogEntity]):
    def __init__(self):
        collection = client.get_collection('blogs')
        self.collection = collection
        super().__init__(collection, BlogEntity)
