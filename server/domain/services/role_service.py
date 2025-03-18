from typing import Optional

from bson import ObjectId
from server.core.types import string
from fastapi import Depends
from server.domain.entities.role_entity import RoleEntity
from server.domain.repositories.role_repository import RoleRepository

class RoleService:
    def __init__(self, role_repository: RoleRepository = Depends()):
        self.role_repository = role_repository

    async def find_one(self, account_id: string) -> Optional[RoleEntity]:
        if not ObjectId.is_valid(account_id):
            return None

        return await self.role_repository.find_one({ "account_id": ObjectId(account_id) })
