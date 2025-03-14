from bson import ObjectId
from fastapi import Depends
from typing import List, Optional, Tuple

from server.core.https import Meta
from server.domain.usecases.tag_usecases import (
    ManageTagUseCase,
    CreateTagReq,
    UpdateTagReq,
)
from server.domain.entities.tag_entity import TagEntity
from server.domain.repositories.tag_repository import TagRepository
from server.core.https import BaseQuery
from server.core.types import string

class TagService(ManageTagUseCase):
    def __init__(self, tag_repository: TagRepository = Depends()):
        self.tag_repository = tag_repository

    async def get_tag(self, id: string) -> TagEntity:
        entity = await self.tag_repository.find_one({"_id": ObjectId(id)})
        if not entity:
            raise Exception("Tag not found")

        return entity

    async def create_tag(self, req: CreateTagReq) -> TagEntity:
        tag = await self.tag_repository.find_with_options({"name": req.name})
        if tag:
            raise Exception("Tag with name already exists, please use another name")

        entity = TagEntity.new(name=req.name)
        return await self.tag_repository.create(entity)

    async def find_with_options(
        self, query: BaseQuery
    ) -> Tuple[List[TagEntity], Meta]:
        response = await self.tag_repository.find_pagination(
            {"name": {"$regex": query.search, "$options": "i"}},
            page=query.page,
            page_size=query.page_size,
        )

        return response

    async def update_tag(self, id: string, body: UpdateTagReq) -> TagEntity:
        response = await self.tag_repository.update(id, body.dict())
        if not response:
            raise Exception("Tag not found")

        return response

    async def delete_tag(self, id: string) -> TagEntity:
        entity = await self.tag_repository.delete(id)
        if not entity:
            raise Exception("Tag not found")

        return entity
