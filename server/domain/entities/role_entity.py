from enum import Enum
from server.core.helpers.time import TimeHelper
from server.domain.entities.base_entity import BaseEntity
from server.core.types import string

class EnumRole(Enum):
    NORMAL = 1
    ADMIN = 1000

class RoleEntity(BaseEntity):
    account_id: string
    role: int

    @staticmethod
    def from_dict(account_id: string, role: EnumRole = EnumRole.NORMAL):
        return RoleEntity(
            id=None,
            account_id=account_id,
            role=role.value,
            created_at=TimeHelper.utc_timezone(),
            updated_at=TimeHelper.utc_timezone(),
            deleted_at=None
        )
