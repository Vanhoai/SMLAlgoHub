from fastapi import Depends

from server.domain.repositories.account_repository import AccountRepository

from server.domain.services.auth_service import AuthService
from server.domain.services.course_service import CourseService
from server.domain.services.account_service import AccountService


async def account_repository() -> AccountRepository:
    return AccountRepository()


async def account_service(
    account_repository: AccountRepository = Depends(account_repository),
) -> AccountService:
    return AccountService(account_repository)


async def auth_service() -> AuthService:
    return AuthService()


async def course_service() -> CourseService:
    return CourseService()
