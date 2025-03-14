from fastapi import Depends

from server.domain.repositories.account_repository import AccountRepository
from server.domain.repositories.course_repository import CourseRepository
from server.domain.repositories.tag_repository import TagRepository
from server.domain.services.auth_service import AuthService
from server.domain.services.course_service import CourseService
from server.domain.services.account_service import AccountService
from server.domain.services.tag_service import TagService

async def account_repository() -> AccountRepository:
    return AccountRepository()

async def tag_repository() -> TagRepository:
    return TagRepository()

async def course_repository() -> CourseRepository:
    return CourseRepository()

async def account_service(
    account_repository: AccountRepository = Depends(account_repository),
) -> AccountService:
    return AccountService(account_repository)

async def auth_service() -> AuthService:
    return AuthService()

async def course_service(
    course_repository: CourseRepository = Depends(course_repository),
) -> CourseService:
    return CourseService(course_repository)

async def tag_service(
    tag_repository: TagRepository = Depends(tag_repository),
) -> TagService:
    return TagService(tag_repository)
