from fastapi import APIRouter, Request, Depends, status

from server.domain.usecases.auth_usecases import SignInReq
from server.domain.services.auth_service import AuthService
from server.core.https import HttpResponse
from server.core.types import string

import server.dependencies as dependencies

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post("/sign-in", response_model=HttpResponse, status_code=status.HTTP_200_OK)
async def sign_in(
    req: Request,
    body: SignInReq,
    auth_service: AuthService = Depends(dependencies.auth_service),
) -> HttpResponse:
    try:
        response = auth_service.sign_in(req=body)
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
