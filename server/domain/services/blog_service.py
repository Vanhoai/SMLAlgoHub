from server.domain.repositories.tag_repository import TagRepository
from typing import List, Optional, Tuple
from bson import ObjectId
from fastapi import Depends
from server.core.exceptions import ErrorCodes, ExceptionHandler
from server.core.https import Meta
from server.domain.entities.blog_entity import BlogEntity
from server.domain.repositories.account_repository import AccountRepository
from server.domain.repositories.blog_repository import BlogRepository
from server.domain.usecases.blog_usecases import CreateBlogReq, FindBlogWithOptionsQuery, ManageBlogUseCase, UpdateBlogReq
from server.core.types import string

class BlogService(ManageBlogUseCase):
    def __init__(
        self,
        blog_repository: BlogRepository = Depends(),
        account_repository: AccountRepository = Depends(),
        tag_repository: TagRepository = Depends()
    ):
        self.blog_repository = blog_repository
        self.account_repository = account_repository
        self.tag_repository = tag_repository

    async def create_blog(self, req: CreateBlogReq) -> BlogEntity:
        # validate
        if not ObjectId.is_valid(req.author_id):
            raise ExceptionHandler(code=ErrorCodes.BAD_REQUEST, msg="Please provide a valid author id")

        if len(req.tags) == 0:
            raise ExceptionHandler(code=ErrorCodes.BAD_REQUEST, msg="Please provide at least one tag")

        for i in range(len(req.tags)):
            if not ObjectId.is_valid(req.tags[i]):
                raise ExceptionHandler(code=ErrorCodes.BAD_REQUEST, msg=f"Tag {req.tags[i]} is not valid")

        # check author
        author = await self.account_repository.find_one({"_id": ObjectId(req.author_id)})
        if not author:
            raise ExceptionHandler(code=ErrorCodes.NOT_FOUND, msg="Author not found")

        # check tags
        tags_query = [ObjectId(tag) for tag in req.tags]

        tags = await self.tag_repository.find_with_options({"_id": {"$in": tags_query}})
        if len(tags) != len(req.tags):
            raise ExceptionHandler(code=ErrorCodes.NOT_FOUND, msg="Some tags not found")

        entity = BlogEntity.new(
            author_id=string(req.author_id),
            thumbnail_url=req.thumbnail_url,
            title=req.title,
            content=req.content,
            count_favourite=0,
            tags=req.tags,
        )

        return await self.blog_repository.create(entity)

    async def update_blog(self, req: UpdateBlogReq) -> BlogEntity: ...

    async def delete_blog(self, id: string) -> BlogEntity: ...

    async def find_blog_by_id(self, id: string) -> Optional[BlogEntity]:
        if not ObjectId.is_valid(id):
            raise ExceptionHandler(code=ErrorCodes.BAD_REQUEST, msg="Please provide a valid blog id")

        return await self.blog_repository.find_one({"id": ObjectId(id)})

    async def find_blogs_by_options(self, query: FindBlogWithOptionsQuery) -> Tuple[List[BlogEntity], Meta]:
        pipeline = []
        match_conditions = {}

        if query.author_id:
            match_conditions["author_id"] = query.author_id

        if query.tags and len(query.tags) > 0:
            match_conditions["tags"] = {"$all": {"$in": query.tags}}

        if query.search:
            match_conditions["$title"] = {"$search": query.search}

        if match_conditions:
            pipeline.append({"$match": match_conditions})

        print("pipline: ", pipeline)

        response = await self.blog_repository.find_pagination({}, page=query.page, page_size=query.page_size)
        return response[0], response[1]
