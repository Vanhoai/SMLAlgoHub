from abc import ABC, abstractmethod
from fastapi_camelcase import CamelModel

from server.core.types import string
from server.domain.entities.account_entity import AccountEntity


class CreateAccountReq(CamelModel):
    username: string
    email: string
    avatar: string
    device_token: string


class ManageAccountUseCase(ABC):
    @abstractmethod
    def create_account(self, req: CreateAccountReq) -> AccountEntity: ...
