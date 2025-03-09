from dependency_injector import containers, providers

class JudgerContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "server.adapters.primary.v1.endpoints.auth",
            "server.adapters.primary.v1.endpoints.accounts"
        ]
    )