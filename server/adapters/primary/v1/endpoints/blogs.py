from fastapi import Depends, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from server import dependencies
from server.adapters.secondary.apis.firebase import OAuthClaims
from server.adapters.shared.middlewares.auth_middleware import auth_middleware
from server.adapters.shared.middlewares.role_middleware import role_middleware
from server.core.exceptions import ErrorCodes, ExceptionHandler
from server.core.https import HttpPaginationResponse, HttpResponse
from server.domain.entities.role_entity import EnumRole
from server.domain.services.blog_service import BlogService
from server.domain.usecases.blog_usecases import CreateBlogReq, FindBlogWithOptionsQuery

from typing import Annotated
from fastapi import APIRouter, Query
from server.core.types import string

router = APIRouter(
    prefix="/blogs",
    tags=["blogs"],
)

@router.post("/")
async def create_blog(
    body: CreateBlogReq,
    claims: OAuthClaims = Depends(auth_middleware),
    _ = Depends(role_middleware(required=[EnumRole.NORMAL])),
    blog_service: BlogService = Depends(dependencies.blog_service),
):
    try:
        blog = await blog_service.create_blog(body)
        response = HttpResponse(
            status_code=status.HTTP_201_CREATED,
            message="success",
            data=blog,
        )

        return JSONResponse(content=jsonable_encoder(response))
    except Exception as exception:
        raise ExceptionHandler(code=ErrorCodes.BAD_REQUEST, msg=string(exception))

@router.get("/")
async def find_blogs(
    query: Annotated[FindBlogWithOptionsQuery, Query()],
    claims: OAuthClaims = Depends(auth_middleware),
    _ = Depends(role_middleware(required=[EnumRole.NORMAL])),
    blog_service: BlogService = Depends(dependencies.blog_service),
):
    try:
        response = await blog_service.find_blogs_by_options(query)

        http_response = HttpPaginationResponse(
            status_code=status.HTTP_200_OK,
            message="success",
            meta=response[1],
            data=response[0],
        )

        return JSONResponse(content=jsonable_encoder(http_response))
    except Exception as exception:
        raise ExceptionHandler(code=ErrorCodes.BAD_REQUEST, msg=string(exception))
