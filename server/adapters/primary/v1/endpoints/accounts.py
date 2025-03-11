from fastapi import APIRouter, status, Depends

from server import dependencies
from server.domain.entities.account_entity import AccountEntity
from server.domain.usecases.account_usecases import CreateAccountReq
from server.domain.services.account_service import AccountService
from server.core.https import HttpResponse
from server.core.types import string
from server.core.exceptions import ExceptionHandler, ErrorCodes

router = APIRouter(
    prefix="/accounts",
    tags=["accounts"],
)


@router.get("/", status_code=status.HTTP_200_OK)
async def get_accounts():
    accounts = AccountEntity.find_all()
    print("accounts: ", accounts)
    return


@router.post("/", status_code=status.HTTP_200_OK, response_model=HttpResponse)
async def create_account(
    body: CreateAccountReq,
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
