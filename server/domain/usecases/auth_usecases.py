from abc import ABC, abstractmethod

class SignInReq:
    pass

class SignInResponse:
    pass

class AuthUseCase(ABC):
    @abstractmethod
    def sign_in(self, req: SignInReq) -> SignInResponse:
        pass
    