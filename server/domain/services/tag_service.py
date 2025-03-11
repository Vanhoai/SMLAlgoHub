from fastapi import Depends
from typing import List, Tuple

from server.core.https import Meta
from server.domain.usecases.tag_usecases import (
    ManageTagUseCase,
    CreateTagReq,
    TagQueryReq,
)
from server.domain.entities.tag_entity import TagEntity
from server.domain.repositories.tag_repository import TagRepository


class TagService(ManageTagUseCase):
    def __init__(self, tag_repository: TagRepository = Depends()):
        self.tag_repository = tag_repository

    async def create_tag(self, req: CreateTagReq) -> TagEntity:
        tag = await self.tag_repository.find_with_options({"name": req.name})
        if tag:
            raise Exception("Tag with name already exists, please use another name")

        return await self.tag_repository.create(req)

    async def find_with_options(
        self, query: TagQueryReq
    ) -> Tuple[List[TagEntity], Meta]:
        response = await self.tag_repository.find_pagination(
            {"name": query.search, "type": query.type},
            page=query.page,
            page_size=query.page_size,
            sort=query.order_by,
        )

        return response
