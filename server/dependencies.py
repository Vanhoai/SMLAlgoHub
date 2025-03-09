from fastapi import Depends

from server.domain.repositories.account_repository import AccountRepository

from server.domain.services.auth_service import AuthService
from server.domain.services.course_service import CourseService


async def account_repository() -> AccountRepository:
    return AccountRepository()


async def auth_service() -> AuthService:
    return AuthService()


async def course_service() -> CourseService:
    return CourseService()
