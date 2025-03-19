from fastapi import APIRouter

from server.adapters.primary.v1.endpoints.accounts import router as accounts_router
from server.adapters.primary.v1.endpoints.auth import router as auth_router
from server.adapters.primary.v1.endpoints.tags import router as tags_router
from server.adapters.primary.v1.endpoints.storages import router as storages_router
from server.adapters.primary.v1.endpoints.blogs import router as blogs_router
from server.adapters.primary.v1.endpoints.problems import router as problems_router
from server.adapters.primary.v1.endpoints.submissions import router as submissions_router

router = APIRouter()
routes = [auth_router, accounts_router, tags_router, storages_router, blogs_router, problems_router, submissions_router]

for route in routes:
    router.include_router(route)
