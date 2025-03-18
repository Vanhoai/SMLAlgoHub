import ast
from typing import List, Optional, Tuple
from bson import ObjectId
from fastapi import Depends

from server.core.https import Meta
from server.domain.usecases.account_usecases import (
    FindAccountsQuery,
    ManageAccountUseCase,
    CreateAccountReq,
)

from server.domain.repositories.account_repository import AccountRepository
from server.domain.entities.account_entity import AccountEntity
from server.core.types import string
from server.core.exceptions import ErrorCodes, ExceptionHandler

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

    async def find_account_by_id(self, id: string) -> Optional[AccountEntity]:
        if not ObjectId.is_valid(id):
            raise ExceptionHandler(code=ErrorCodes.NOT_FOUND, msg="Can not find account")

        return await self.account_repository.find_one({"_id": ObjectId(id)})

    async def find_accounts(self, query: FindAccountsQuery) -> Tuple[List[AccountEntity], Meta]:
        response = await self.account_repository.find_pagination(
            {},
            page=query.page,
            page_size=query.page_size
        )

        return response

    async def find_account_with_email(self, email: string) -> Optional[AccountEntity]:
        return await self.account_repository.find_one({"email": email})
