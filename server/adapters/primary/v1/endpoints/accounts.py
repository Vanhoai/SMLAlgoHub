from typing import Annotated
from fastapi import APIRouter, Query, status, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from server import dependencies
from server.adapters.secondary.apis.firebase import OAuthClaims
from server.adapters.shared.middlewares.auth_middleware import auth_middleware
from server.adapters.shared.middlewares.role_middleware import role_middleware
from server.domain.entities.role_entity import EnumRole
from server.domain.usecases.account_usecases import CreateAccountReq, FindAccountsQuery
from server.domain.services.account_service import AccountService
from server.core.https import HttpPaginationResponse, HttpResponse
from server.core.types import string
from server.core.exceptions import ExceptionHandler, ErrorCodes

router = APIRouter(
    prefix="/accounts",
    tags=["accounts"],
)

@router.get("/", status_code=status.HTTP_200_OK)
async def get_accounts(
    query: Annotated[FindAccountsQuery, Query()],
    claims: OAuthClaims = Depends(auth_middleware),
    _ = Depends(role_middleware(required=[EnumRole.NORMAL])),
    account_service: AccountService = Depends(dependencies.account_service),
) -> JSONResponse:
    try:
        response = await account_service.find_accounts(query)
        http_response = HttpPaginationResponse(
            status_code=status.HTTP_200_OK,
            message="success",
            meta=response[1],
            data=response[0],
        )

        return JSONResponse(content=jsonable_encoder(http_response))
    except Exception as exception:
        raise ExceptionHandler(code=ErrorCodes.BAD_REQUEST, msg=string(exception))

@router.post("/", status_code=status.HTTP_200_OK, response_model=HttpResponse)
async def create_account(
    body: CreateAccountReq,
    claims: OAuthClaims = Depends(auth_middleware),
    _ = Depends(role_middleware(required=[EnumRole.NORMAL])),
    account_service: AccountService = Depends(dependencies.account_service),
) -> HttpResponse:
    try:
        response = await account_service.create_account(req=body)
        return HttpResponse(
            status_code=status.HTTP_200_OK,
            message="success",
            data=response,
        )
    except Exception as exception:
        raise ExceptionHandler(code=ErrorCodes.BAD_REQUEST, msg=string(exception))
