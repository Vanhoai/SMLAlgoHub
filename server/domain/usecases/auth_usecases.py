from abc import ABC, abstractmethod
from fastapi_camelcase import CamelModel
from pydantic import BaseModel

from server.core.types import string


class PushNotificationUseCase:
    pass


class SignInReq(BaseModel):
    email: string
    password: string


class SignInResponse(CamelModel):
    access_token: string
    refresh_token: string


class AuthUseCase(ABC):
    @abstractmethod
    def sign_in(self, req: SignInReq) -> SignInResponse: ...
