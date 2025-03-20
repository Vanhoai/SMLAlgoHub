from fastapi import APIRouter, Request, Depends

from server.domain.usecases.auth_usecases import SignInReq
from server.domain.services.auth_service import AuthService
from server.core.https import HttpResponse
from server.core.types import string

import server.dependencies as dependencies

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post("/oauth")
async def oauth(
    req: Request,
    body: SignInReq,
    auth_service: AuthService = Depends(dependencies.auth_service),
) -> HttpResponse:
    try:
        response = await auth_service.sign_in(req=body)
        return HttpResponse(
            status_code=200,
            message="success",
            data=response,
        )

    except Exception as exception:
        return HttpResponse(
            status_code=400,
            message=string(exception),
        )
