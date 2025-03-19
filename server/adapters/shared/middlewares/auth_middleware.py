from fastapi import Depends, Request
from firebase_admin import auth
from server import dependencies
from server.adapters.secondary.apis.firebase import OAuthClaims
from server.core.exceptions import ErrorCodes, ExceptionHandler
from server.domain.entities.account_entity import AccountEntity
from server.domain.services.account_service import AccountService

async def require_token(req: Request) -> OAuthClaims:
    authorization = req.headers["Authorization"]
    strs = authorization.split(" ")
    if len(strs) != 2:
        raise ExceptionHandler(code=ErrorCodes.UNAUTHORIZED, msg="Invalid authorization header format.")

    tokenType = strs[0]
    if tokenType != "Bearer":
        raise ExceptionHandler(code=ErrorCodes.UNAUTHORIZED, msg="Ensure use of Bearer token.")

    accessToken = strs[1]
    if not accessToken:
        raise ExceptionHandler(code=ErrorCodes.UNAUTHORIZED, msg="Please provide a valid access token.")

    claims = auth.verify_id_token(accessToken)
    response = OAuthClaims.validate(claims)
    return response

async def auth_middleware(
    req: Request,
    account_service: AccountService = Depends(dependencies.account_service)
) -> AccountEntity:
    try:
        response = await require_token(req)
        account = await account_service.find_account_with_email(response.email)
        if not account:
            raise ExceptionHandler(code=ErrorCodes.UNAUTHORIZED, msg="Account not found in database")

        req.state.account = account
        return account
    except Exception as exception:
        raise ExceptionHandler(code=ErrorCodes.UNAUTHORIZED, msg=str(exception))
