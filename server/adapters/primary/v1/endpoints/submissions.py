import asyncio
from typing import Annotated
from fastapi import APIRouter, Depends, Query, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.background import BackgroundTasks

from server.core.exceptions import ErrorCodes, ExceptionHandler
from server.core.https import HttpPaginationResponse, HttpResponse
from server.domain.services.submission_service import SubmissionService
from server.domain.services.problem_service import ProblemService
from server.domain.usecases.submission_usecases import (
    CreateSubmissionReq,
    FindSubmissionsQuery,
    GradingSubmissionReq,
)
from server.adapters.secondary.apis.firebase import OAuthClaims
from server import dependencies
from server.adapters.shared.middlewares.auth_middleware import auth_middleware
from server.adapters.shared.middlewares.role_middleware import role_middleware
from server.core.types import string
from server.celery_process import process_submission, process_submission_async

router = APIRouter(
    prefix="/submissions",
    tags=["submissions"],
)


@router.post("/grading")
async def grade_submission(
    body: GradingSubmissionReq,
    claims: OAuthClaims = Depends(auth_middleware),
    _=Depends(role_middleware(required=[])),
    submission_service: SubmissionService = Depends(dependencies.submission_service),
):
    try:
        submission = await submission_service.grading_submission(body)
        response = HttpResponse(
            status_code=status.HTTP_201_CREATED,
            message="Submission created successfully",
            data=submission,
        )

        return JSONResponse(content=jsonable_encoder(response))
    except Exception as exception:
        if isinstance(exception, ExceptionHandler):
            raise exception

        raise ExceptionHandler(code=ErrorCodes.BAD_REQUEST, msg=string(exception))


@router.post("/")
async def create_submission(
    body: CreateSubmissionReq,
    background_tasks: BackgroundTasks,
    claims: OAuthClaims = Depends(auth_middleware),
    _=Depends(role_middleware(required=[])),
    submission_service: SubmissionService = Depends(dependencies.submission_service),
    problem_service: ProblemService = Depends(dependencies.problem_service),
):
    try:
        submission = await submission_service.create_submission(body)
        response = HttpResponse(
            status_code=status.HTTP_201_CREATED,
            message="Submission created successfully",
            data=submission,
        )

        # process_submission.delay(submission_id=submission.id)
        background_tasks.add_task(
            process_submission_async,
            submission_entity=submission,
            submission_service=submission_service,
            problem_service=problem_service,
        )

        return JSONResponse(content=jsonable_encoder(response))
    except Exception as exception:
        if isinstance(exception, ExceptionHandler):
            raise exception

        raise ExceptionHandler(code=ErrorCodes.BAD_REQUEST, msg=string(exception))


@router.get("/")
async def find_submissions(
    query: Annotated[FindSubmissionsQuery, Query()],
    claims: OAuthClaims = Depends(auth_middleware),
    _=Depends(role_middleware(required=[])),
    submission_service: SubmissionService = Depends(dependencies.submission_service),
):
    try:
        payload = await submission_service.find_submissions(query)
        response = HttpPaginationResponse(
            status_code=status.HTTP_200_OK,
            message="success",
            meta=payload[1],
            data=payload[0],
        )

        return JSONResponse(content=jsonable_encoder(response))
    except Exception as exception:
        if isinstance(exception, ExceptionHandler):
            raise exception
        raise ExceptionHandler(code=ErrorCodes.BAD_REQUEST, msg=string(exception))
