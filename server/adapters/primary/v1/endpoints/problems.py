from typing import Annotated
from fastapi import APIRouter, Depends, Query, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from server import dependencies
from server.adapters.secondary.apis.firebase import OAuthClaims
from server.adapters.shared.middlewares.auth_middleware import auth_middleware
from server.adapters.shared.middlewares.role_middleware import role_middleware
from server.core.exceptions import ErrorCodes, ExceptionHandler
from server.core.https import HttpPaginationResponse, HttpResponse
from server.domain.entities.role_entity import EnumRole
from server.domain.services.problem_service import ProblemService
from server.domain.usecases.problem_usecases import (
    CreateProblemReq,
    FindProblemsQuery,
    UpdateProblemReq,
)
from server.core.types import string

router = APIRouter(
    prefix="/problems",
    tags=["problems"],
)


@router.post("/")
async def create_problem(
    body: CreateProblemReq,
    claims: OAuthClaims = Depends(auth_middleware),
    _=Depends(role_middleware(required=[EnumRole.NORMAL])),
    problem_service: ProblemService = Depends(dependencies.problem_service),
):
    try:
        problem = await problem_service.create_problem(body)
        response = HttpResponse(
            status_code=status.HTTP_201_CREATED,
            message="Problem created",
            data=problem,
        )

        return JSONResponse(content=jsonable_encoder(response))
    except Exception as exception:
        raise ExceptionHandler(code=ErrorCodes.BAD_REQUEST, msg=string(exception))


@router.put("/{id}")
async def update_problem(
    id: string,
    body: UpdateProblemReq,
    claims: OAuthClaims = Depends(auth_middleware),
    _=Depends(role_middleware(required=[EnumRole.NORMAL])),
    problem_service: ProblemService = Depends(dependencies.problem_service),
):
    return {"message": "Problem updated"}


@router.get("/")
async def find_problems(
    query: Annotated[FindProblemsQuery, Query()],
    claims: OAuthClaims = Depends(auth_middleware),
    _=Depends(role_middleware(required=[])),
    problem_service: ProblemService = Depends(dependencies.problem_service),
):
    try:
        payload = await problem_service.find_problems(query)
        response = HttpPaginationResponse(
            status_code=status.HTTP_200_OK,
            message="success",
            meta=payload[1],
            data=payload[0],
        )

        return JSONResponse(content=jsonable_encoder(response))

    except Exception as exception:
        raise ExceptionHandler(code=ErrorCodes.BAD_REQUEST, msg=string(exception))


@router.post("/fake")
async def fake(
    body: CreateProblemReq,
    claims: OAuthClaims = Depends(auth_middleware),
    _=Depends(role_middleware(required=[EnumRole.NORMAL])),
    problem_service: ProblemService = Depends(dependencies.problem_service),
):
    await problem_service.fake(body)
    return {"message": "Fake success"}


@router.get("/{id}")
async def find_problem(
    id: string,
    claims: OAuthClaims = Depends(auth_middleware),
    _=Depends(role_middleware(required=[EnumRole.NORMAL])),
    problem_service: ProblemService = Depends(dependencies.problem_service),
):
    try:
        problem = await problem_service.find_problem(id)
        response = HttpResponse(
            status_code=status.HTTP_200_OK,
            message="Problem found",
            data=problem,
        )

        return JSONResponse(content=jsonable_encoder(response))
    except Exception as exception:
        raise ExceptionHandler(code=ErrorCodes.BAD_REQUEST, msg=string(exception))
