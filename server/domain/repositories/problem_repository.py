from typing import List, Optional, Tuple

from bson import ObjectId
from server.core.https import Meta
from server.domain.aggregates.problem_aggregate import (
    ProblemAggregate,
    ProblemAggregateDetail,
    ProblemBase,
)
from server.domain.entities.problem_entity import ProblemEntity
from server.domain.entities.tag_entity import TagEntity
from server.domain.repositories.base_repository import BaseRepository
from server.database import client
from server.domain.usecases.problem_usecases import FindProblemsQuery
from server.core.types import string


class ProblemRepository(BaseRepository[ProblemEntity]):
    def __init__(self):
        collection = client.get_collection("problems")
        self.collection = collection
        super().__init__(collection, ProblemEntity)

    async def create_problem(self, problem: ProblemEntity) -> ProblemEntity:
        tags = [ObjectId(tag) for tag in problem.tags]

        data = problem.dict(exclude={"id"})
        data["tags"] = tags

        for key, value in data.items():
            if "_id" in key:
                data[key] = ObjectId(value)

        result = await self.collection.insert_one(data)
        data["id"] = string(result.inserted_id)

        for key, value in data.items():
            if ObjectId.is_valid(value):
                data[key] = string(value)

        data["tags"] = problem.tags
        return self.model.model_validate(data)

    async def find_base(self, id: string) -> Optional[ProblemBase]:
        doc = await self.collection.find_one({"_id": ObjectId(id)})
        if not doc:
            return None

        doc["id"] = str(doc["_id"])
        return ProblemBase(**doc)

    async def find_problems_pagination(
        self, query: FindProblemsQuery
    ) -> Tuple[List[ProblemAggregate], Meta]:
        skip = (query.page - 1) * query.page_size

        match_stage = {}

        if query.search:
            match_stage["$or"] = [
                {"title": {"$regex": query.search, "$options": "i"}},
            ]

        # Nếu có lọc theo levels
        if query.levels and len(query.levels) > 0:
            match_stage["level"] = {"$in": [level.value for level in query.levels]}

        # Nếu có lọc theo tags
        if query.tags and len(query.tags) > 0:
            match_stage["tags"] = {"$all": query.tags}

        pipeline = [
            {"$match": {"deletedAt": {"$eq": None}}},
            {"$skip": skip},
            {"$limit": query.page_size},
            {
                "$lookup": {
                    "from": "tags",
                    "localField": "tags",
                    "foreignField": "_id",
                    "as": "tags_information",
                }
            },
            {
                "$lookup": {
                    "from": "accounts",
                    "localField": "author_id",
                    "foreignField": "_id",
                    "as": "author",
                }
            },
            {"$unwind": {"path": "$author", "preserveNullAndEmptyArrays": True}},
        ]

        result = await self.collection.aggregate(pipeline).to_list(length=None)
        problems = [
            ProblemAggregate(
                **{
                    **item,
                    "id": str(item["_id"]),
                    "tags": [
                        TagEntity(**{**tag, "id": str(tag["_id"])})
                        for tag in item["tags_information"]
                    ],
                }
            )
            for item in result
        ]

        return problems, Meta.empty()

    async def find_problem(self, id: string) -> Optional[ProblemAggregateDetail]:
        pipeline = [
            {"$match": {"_id": ObjectId(id)}},
            {
                "$lookup": {
                    "from": "tags",
                    "localField": "tags",
                    "foreignField": "_id",
                    "as": "tags_information",
                }
            },
            {
                "$lookup": {
                    "from": "accounts",
                    "localField": "author_id",
                    "foreignField": "_id",
                    "as": "author",
                }
            },
            {"$unwind": {"path": "$author", "preserveNullAndEmptyArrays": True}},
        ]

        result = await self.collection.aggregate(pipeline).to_list(length=None)
        problems = [
            ProblemAggregateDetail(
                **{
                    **item,
                    "id": str(item["_id"]),
                    "author_id": str(item["author_id"]),
                    "author": {**item["author"], "id": str(item["author"]["_id"])},
                    "tags": [
                        TagEntity(**{**tag, "id": str(tag["_id"])})
                        for tag in item["tags_information"]
                    ],
                }
            )
            for item in result
        ]

        problem = problems[0] if problems else None
        return problem
