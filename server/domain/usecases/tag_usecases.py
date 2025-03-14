from abc import ABC, abstractmethod
from pydantic.types import Tag
from typing_extensions import Optional
from fastapi_camelcase import CamelModel
from typing import Tuple, List

from server.core.types import string
from server.domain.entities.tag_entity import TagEntity
from server.core.https import BaseQuery, Meta

class CreateTagReq(CamelModel):
    name: string

class UpdateTagReq(CamelModel):
    name: string

class ManageTagUseCase(ABC):
    @abstractmethod
    async def create_tag(self, req: CreateTagReq) -> TagEntity: ...
    @abstractmethod
    async def find_with_options(self, query: BaseQuery) -> Tuple[List[TagEntity], Meta]: ...
    @abstractmethod
    async def update_tag(self, id: string, body: UpdateTagReq) -> TagEntity: ...
    @abstractmethod
    async def delete_tag(self, id: string) -> TagEntity: ...
    @abstractmethod
    async def get_tag(self, id: string) -> TagEntity: ...
