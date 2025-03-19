from server.core.types import string
from cloudinary import uploader, api
from typing import List

class CloudinaryApi:
    @staticmethod
    def upload(file: bytes):
        return uploader.upload(file)

    @staticmethod
    def delete(ids: List[string]):
        results = api.delete_resources(ids, resource_type="image", type="upload")
        return results
