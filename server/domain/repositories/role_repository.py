from server.domain.repositories.base_repository import BaseRepository
from server.domain.entities.role_entity import RoleEntity
from server.database import client

class RoleRepository(BaseRepository[RoleEntity]):
    def __init__(self):
        collection = client.get_collection("roles")
        self.collection = collection
        super().__init__(collection, RoleEntity)
