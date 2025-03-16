from fastapi import APIRouter, UploadFile
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse

from server.adapters.secondary.apis.cloudinary import CloudinaryApi
from server.core.exceptions import ErrorCodes, ExceptionHandler
from server.core.types import string

router = APIRouter(
    prefix="/storages",
    tags=["storages"],
)

@router.post("/upload")
async def upload_file(file: UploadFile):
    try:
        if not file.size or  file.size > 500 * 1024: # 500 KB
            raise ExceptionHandler(code=ErrorCodes.FILE_SIZE_EXCEEDED, msg="File size exceeds limit")

        bytes_data = await file.read()
        uploaded = CloudinaryApi.upload(bytes_data)
        return JSONResponse(content=jsonable_encoder(uploaded))
    except Exception as exception:
        if isinstance(exception, HTTPException):
            raise exception

        raise ExceptionHandler(code=ErrorCodes.BAD_REQUEST, msg=string(exception))
