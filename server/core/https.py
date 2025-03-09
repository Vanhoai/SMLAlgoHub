from fastapi_camelcase import CamelModel
from typing import Any

from server.core.types import string


class HttpResponse(CamelModel):
    status_code: int
    message: string
    data: Any
