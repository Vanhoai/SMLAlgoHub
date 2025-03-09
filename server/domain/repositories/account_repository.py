from server.domain.repositories.base_repository import BaseRepository
from server.domain.entities.account_entity import AccountEntity

class AccountRepository(BaseRepository[AccountEntity]):
    def __init__(self):
        super().__init__(AccountEntity)
