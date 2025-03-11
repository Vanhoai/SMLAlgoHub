from server.domain.repositories.base_repository import BaseRepository
from server.domain.entities.tag_entity import TagEntity


class TagRepository(BaseRepository[TagEntity]):
    def __init__(self):
        super().__init__(TagEntity)
