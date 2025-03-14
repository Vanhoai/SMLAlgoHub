from fastapi import APIRouter, Depends, status, Query
from typing import Annotated

from server import dependencies
from server.core.https import HttpPaginationResponse, HttpResponse, BaseQuery
from server.core.exceptions import ExceptionHandler, ErrorCodes
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from server.core.types import string
from server.domain.services.tag_service import TagService
from server.domain.usecases.tag_usecases import CreateTagReq, UpdateTagReq

router = APIRouter(
    prefix="/tags",
    tags=["tags"],
)

@router.put("/{id}")
async def update_tag(
    id: str,
    body: UpdateTagReq,
    tag_service: TagService = Depends(dependencies.tag_service),
):
    try:
        response = await tag_service.update_tag(id, body)
        return HttpResponse(status_code=status.HTTP_200_OK, message="success", data=response)
    except Exception as exception:
        raise ExceptionHandler(code=ErrorCodes.BAD_REQUEST, msg=string(exception))

@router.delete("/{id}")
async def delete_tag(
    id: str,
    tag_service: TagService = Depends(dependencies.tag_service),
):
    try:
        response = await tag_service.delete_tag(id)
        return HttpResponse(status_code=status.HTTP_200_OK, message="success", data=response)
    except Exception as exception:
        raise ExceptionHandler(code=ErrorCodes.BAD_REQUEST, msg=string(exception))

@router.post("/")
async def create_tag(
    body: CreateTagReq,
    tag_service: TagService = Depends(dependencies.tag_service),
):
    try:
        response = await tag_service.create_tag(body)
        return HttpResponse(status_code=status.HTTP_200_OK, message="success", data=response)
    except Exception as exception:
        raise ExceptionHandler(code=ErrorCodes.BAD_REQUEST, msg=string(exception))

@router.get("/{id}")
async def get_tag(
    id: str,
    tag_service: TagService = Depends(dependencies.tag_service),
):
    try:
        response = await tag_service.get_tag(id)
        return HttpResponse(status_code=status.HTTP_200_OK, message="success", data=response)
    except Exception as exception:
        raise ExceptionHandler(code=ErrorCodes.BAD_REQUEST, msg=string(exception))

@router.get("/")
async def find_tags(
    query: Annotated[BaseQuery, Query()],
    tag_service: TagService = Depends(dependencies.tag_service),
) -> JSONResponse:
    try:
        response = await tag_service.find_with_options(query)

        http_response = HttpPaginationResponse(
            status_code=status.HTTP_200_OK,
            message="success",
            meta=response[1],
            data=response[0],
        )

        return JSONResponse(content=jsonable_encoder(http_response))
    except Exception as exception:
        raise ExceptionHandler(code=ErrorCodes.BAD_REQUEST, msg=string(exception))
