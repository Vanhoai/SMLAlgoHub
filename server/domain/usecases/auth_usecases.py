from abc import ABC, abstractmethod
from pydantic import BaseModel

from server.core.types import string

class SignInReq(BaseModel):
    email: string
    password: string

class SignInResponse:
    pass

class AuthUseCase(ABC):
    @abstractmethod
    def sign_in(self, req: SignInReq) -> SignInResponse:
        pass
    