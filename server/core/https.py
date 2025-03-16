from fastapi_camelcase import CamelModel
from pydantic import  Field
from typing import Any, Literal

from server.core.types import string

class BaseQuery(CamelModel):
    page: int = Field(1, gt=0, le=50)
    page_size: int = Field(30, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    search: string = ""

class HttpResponse(CamelModel):
    status_code: int
    message: string
    data: Any = None

class Meta(CamelModel):
    page: int
    page_size: int
    total_page: int
    total_record: int

    @staticmethod
    def empty():
        return Meta(page=1, page_size=30, total_page=1, total_record=0)

class HttpPaginationResponse(CamelModel):
    status_code: int
    message: string
    meta: Meta
    data: Any = None
