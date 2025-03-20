from fastapi import Depends

from server.domain.repositories.account_repository import AccountRepository
from server.domain.repositories.blog_repository import BlogRepository
from server.domain.repositories.course_repository import CourseRepository
from server.domain.repositories.problem_repository import ProblemRepository
from server.domain.repositories.role_repository import RoleRepository
from server.domain.repositories.tag_repository import TagRepository
from server.domain.repositories.submission_repository import SubmissionRepository

from server.domain.services.auth_service import AuthService
from server.domain.services.blog_service import BlogService
from server.domain.services.course_service import CourseService
from server.domain.services.account_service import AccountService
from server.domain.services.problem_service import ProblemService
from server.domain.services.role_service import RoleService
from server.domain.services.tag_service import TagService
from server.domain.services.submission_service import SubmissionService


async def account_repository() -> AccountRepository:
    return AccountRepository()


async def role_repository() -> RoleRepository:
    return RoleRepository()


async def tag_repository() -> TagRepository:
    return TagRepository()


async def course_repository() -> CourseRepository:
    return CourseRepository()


async def blog_repository() -> BlogRepository:
    return BlogRepository()


async def problem_repository() -> ProblemRepository:
    return ProblemRepository()


async def submission_repository() -> SubmissionRepository:
    return SubmissionRepository()


async def account_service(
    account_repository: AccountRepository = Depends(account_repository),
) -> AccountService:
    return AccountService(account_repository)


async def auth_service(
    account_repository: AccountRepository = Depends(account_repository),
) -> AuthService:
    return AuthService(account_repository)


async def role_service(
    role_repository: RoleRepository = Depends(role_repository),
) -> RoleService:
    return RoleService(role_repository)


async def course_service(
    course_repository: CourseRepository = Depends(course_repository),
) -> CourseService:
    return CourseService(course_repository)


async def tag_service(
    tag_repository: TagRepository = Depends(tag_repository),
) -> TagService:
    return TagService(tag_repository)


async def blog_service(
    blog_repository: BlogRepository = Depends(blog_repository),
    account_repository: AccountRepository = Depends(account_repository),
    tag_repository: TagRepository = Depends(tag_repository),
) -> BlogService:
    return BlogService(blog_repository, account_repository, tag_repository)


async def problem_service(
    problem_repository: ProblemRepository = Depends(problem_repository),
    account_repository: AccountRepository = Depends(account_repository),
    tag_repository: TagRepository = Depends(tag_repository),
) -> ProblemService:
    return ProblemService(problem_repository, account_repository, tag_repository)


async def submission_service(
    submission_repository: SubmissionRepository = Depends(submission_repository),
    account_repository: AccountRepository = Depends(account_repository),
    problem_repository: ProblemRepository = Depends(problem_repository),
) -> SubmissionService:
    return SubmissionService(
        submission_repository, problem_repository, account_repository
    )
