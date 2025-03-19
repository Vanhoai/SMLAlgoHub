from server.core.https import BaseQuery, Meta
from server.core.types import string
from abc import ABC, abstractmethod
from typing import List, Optional, Tuple
from fastapi_camelcase import CamelModel

from server.domain.entities.blog_entity import BlogEntity

class CreateBlogReq(CamelModel):
    author_id: Optional[string]
    thumbnail_url: string
    title: string
    content: string
    tags: List[string]

class UpdateBlogReq(CamelModel):
    id: string
    thumbnail_url: string
    title: string
    content: string
    tags: List[string]

class FindBlogWithOptionsQuery(BaseQuery):
    author_id: Optional[string] = None
    tags: List[string] = []

class ManageBlogUseCase(ABC):
    @abstractmethod
    async def create_blog(self, req: CreateBlogReq) -> BlogEntity: ...
    @abstractmethod
    async def update_blog(self, req: UpdateBlogReq) -> BlogEntity: ...
    @abstractmethod
    async def delete_blog(self, id: string) -> BlogEntity: ...
    @abstractmethod
    async def find_blog_by_id(self, id: string) -> Optional[BlogEntity]: ...
    @abstractmethod
    async def find_blogs_by_options(self, query: FindBlogWithOptionsQuery) -> Tuple[List[BlogEntity], Meta]: ...
