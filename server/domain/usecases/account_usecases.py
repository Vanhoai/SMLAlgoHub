from abc import ABC, abstractmethod
from typing import List, Optional, Tuple
from fastapi_camelcase import CamelModel

from server.core.https import BaseQuery, Meta
from server.core.types import string
from server.domain.entities.account_entity import AccountEntity


class CreateAccountReq(CamelModel):
    username: string
    email: string
    avatar: string
    device_token: string

class FindAccountsQuery(BaseQuery):
    pass

class ManageAccountUseCase(ABC):
    @abstractmethod
    async def create_account(self, req: CreateAccountReq) -> AccountEntity: ...

    @abstractmethod
    async def find_account_by_id(self, id: string) -> Optional[AccountEntity]: ...

    @abstractmethod
    async def find_accounts(self, query: FindAccountsQuery) -> Tuple[List[AccountEntity], Meta]: ...

    @abstractmethod
    async def find_account_with_email(self, email: string) -> Optional[AccountEntity]: ...
