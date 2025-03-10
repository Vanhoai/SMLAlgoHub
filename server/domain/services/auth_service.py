from server.domain.usecases.auth_usecases import (
    AuthUseCase,
    PushNotificationUseCase,
    SignInReq,
    SignInResponse,
)


class AuthService(AuthUseCase, PushNotificationUseCase):
    def sign_in(self, req: SignInReq) -> SignInResponse:
        print(req)
        return SignInResponse(
            access_token="access_token",
            refresh_token="refresh_token",
        )
