from server.core.services import BaseService

from server.domain.usecases.auth_usecases import AuthUseCase, SignInReq, SignInResponse


class AuthService(BaseService, AuthUseCase):
    def sign_in(self, req: SignInReq) -> SignInResponse:
        print(req)
        return SignInResponse(
            access_token="access_token",
            refresh_token="refresh_token",
        )
