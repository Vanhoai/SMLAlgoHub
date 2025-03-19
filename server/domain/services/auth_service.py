from fastapi import Depends
from server.adapters.secondary.apis.firebase import OAuthClaims
from server.domain.entities.account_entity import AccountEntity
from server.domain.repositories.account_repository import AccountRepository
from server.domain.usecases.auth_usecases import (
    AuthUseCase,
    PushNotificationUseCase,
    SignInReq,
)
from firebase_admin import auth

class AuthService(AuthUseCase, PushNotificationUseCase):
    def __init__(self, account_repository: AccountRepository = Depends()):
        self.account_repository = account_repository

    async def sign_in(self, req: SignInReq) -> AccountEntity:
        claims = auth.verify_id_token(req.id_token)
        model = OAuthClaims.validate(claims)

        # check account exist -> if not -> create new account
        account = await self.account_repository.find_one({ "email": model.email })
        if not account:
            entity = AccountEntity.new(
                username=model.name,
                email=model.email,
                avatar=model.picture,
                device_token=req.device_token,
            )

            account = await self.account_repository.create(entity)

        return account
