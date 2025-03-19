from server.domain.repositories.base_repository import BaseRepository
from server.domain.entities.tag_entity import TagEntity
from server.database import client

class TagRepository(BaseRepository[TagEntity]):
    def __init__(self):
        collection = client.get_collection("tags")
        super().__init__(collection, TagEntity)
