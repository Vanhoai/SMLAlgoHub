from dependency_injector import containers, providers

from server.domain.repositories.account_repository import AccountRepository

from server.domain.services.auth_service import AuthService
from server.domain.services.course_service import CourseService

class MLAlgoHubContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "server.adapters.primary.v1.endpoints.auth",
            "server.adapters.primary.v1.endpoints.accounts"
        ]
    )

    # Repositories
    account_repository = providers.Singleton(AccountRepository)

    # Services
    account_service = providers.Singleton(AuthService)
    course_service = providers.Singleton(CourseService)

    print("Container initialized")