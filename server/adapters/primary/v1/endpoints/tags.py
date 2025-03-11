from fastapi import APIRouter, status, Query
from typing import Annotated

from server.core.https import HttpResponse
from server.core.exceptions import ExceptionHandler, ErrorCodes
from server.domain.usecases.tag_usecases import TagQueryReq

from server.core.types import string

router = APIRouter(
    prefix="/tags",
    tags=["tags"],
)


@router.post("/", status_code=status.HTTP_200_OK, response_model=HttpResponse)
async def create_tag():
    pass


@router.get("/", status_code=status.HTTP_200_OK, response_model=HttpResponse)
async def find_tags(query: Annotated[TagQueryReq, Query()]) -> HttpResponse:
    try:
        return HttpResponse(status_code=status.HTTP_200_OK, message="success")
    except Exception as exception:
        raise ExceptionHandler(code=ErrorCodes.BAD_REQUEST, msg=string(exception))
