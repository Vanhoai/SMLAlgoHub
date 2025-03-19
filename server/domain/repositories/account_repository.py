from server.database import client
from server.domain.repositories.base_repository import BaseRepository
from server.domain.entities.account_entity import AccountEntity

class AccountRepository(BaseRepository[AccountEntity]):
    def __init__(self):
        collection = client.get_collection('accounts')
        super().__init__(collection, AccountEntity)
