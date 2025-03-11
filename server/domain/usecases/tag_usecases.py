from abc import ABC, abstractmethod
from fastapi_camelcase import CamelModel
from pydantic import Field
from typing import Literal, Tuple, List

from server.core.types import string
from server.domain.entities.tag_entity import TagEntity
from server.core.https import BaseQuery, Meta


class CreateTagReq(CamelModel):
    name: string
    type: Literal[1, 2] = 1


class TagQueryReq(BaseQuery):
    type: Literal[0, 1, 2] = 0


class ManageTagUseCase(ABC):
    @abstractmethod
    def create_tag(self, req: CreateTagReq) -> TagEntity: ...
    @abstractmethod
    def find_with_options(self, query: TagQueryReq) -> Tuple[List[TagEntity], Meta]: ...
