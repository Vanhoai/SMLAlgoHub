from fastapi import Depends

from server.domain.usecases.account_usecases import (
    ManageAccountUseCase,
    CreateAccountReq,
)

from server.domain.repositories.account_repository import AccountRepository
from server.domain.entities.account_entity import AccountEntity


class AccountService(ManageAccountUseCase):
    def __init__(self, account_repository: AccountRepository = Depends()):
        self.account_repository = account_repository

    async def create_account(self, req: CreateAccountReq) -> AccountEntity:
        account = await self.account_repository.find_with_options({"email": req.email})
        if account:
            raise Exception("Account already exists")

        entity = AccountEntity.new(
            username=req.username,
            email=req.email,
            avatar=req.avatar,
            device_token=req.device_token,
        )

        return await self.account_repository.create(entity)
