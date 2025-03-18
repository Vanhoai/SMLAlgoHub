from abc import ABC, abstractmethod
from fastapi_camelcase import CamelModel

from server.core.types import string
from server.domain.entities.account_entity import AccountEntity

class PushNotificationUseCase:
    pass

class SignInReq(CamelModel):
    id_token: string
    device_token: string

class SignInResponse(CamelModel):
    access_token: string
    refresh_token: string

class AuthUseCase(ABC):
    @abstractmethod
    async def sign_in(self, req: SignInReq) -> AccountEntity: ...
