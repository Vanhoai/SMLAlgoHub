from fastapi import APIRouter

from server.adapters.primary.v1.endpoints.accounts import router as accounts_router
from server.adapters.primary.v1.endpoints.auth import router as auth_router
from server.adapters.primary.v1.endpoints.tags import router as tags_router

router = APIRouter()
routes = [auth_router, accounts_router, tags_router]

for route in routes:
    route.tags = route.tags.append("v1")
    router.include_router(route)
