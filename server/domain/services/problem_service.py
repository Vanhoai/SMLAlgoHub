from typing import List, Tuple
from bson import ObjectId
from fastapi import Depends

from server.core.exceptions import ErrorCodes, ExceptionHandler
from server.core.types import string
from server.core.https import Meta
from server.domain.aggregates.problem_aggregate import (
    ProblemAggregate,
    ProblemAggregateDetail,
)
from server.domain.entities.problem_entity import IOMode, ProblemEntity, ProblemLevel
from server.domain.repositories.account_repository import AccountRepository
from server.domain.repositories.problem_repository import ProblemRepository
from server.domain.repositories.tag_repository import TagRepository
from server.domain.usecases.problem_usecases import (
    CreateProblemReq,
    FindProblemsQuery,
    ManageProblemUseCases,
    UpdateProblemReq,
)
import random


class ProblemService(ManageProblemUseCases):
    def __init__(
        self,
        problem_repository: ProblemRepository = Depends(),
        account_repository: AccountRepository = Depends(),
        tag_repository: TagRepository = Depends(),
    ):
        self.problem_repository = problem_repository
        self.account_repository = account_repository
        self.tag_repository = tag_repository

    async def create_problem(self, req: CreateProblemReq) -> ProblemEntity:
        if not ObjectId.is_valid(req.author_id):
            raise ExceptionHandler(
                code=ErrorCodes.BAD_REQUEST, msg="Please provide a valid author ID"
            )

        if not req.tags or len(req.tags) <= 0:
            raise ExceptionHandler(
                code=ErrorCodes.BAD_REQUEST, msg="Please provide at least one tag"
            )

        if req.level not in ProblemLevel:
            raise ExceptionHandler(
                code=ErrorCodes.BAD_REQUEST, msg="Please provide a valid level"
            )

        if req.io_mode not in IOMode:
            raise ExceptionHandler(
                code=ErrorCodes.BAD_REQUEST, msg="Please provide a valid io mode"
            )

        # check valid in database
        tags_query = [ObjectId(tag) for tag in req.tags]
        tags = await self.tag_repository.find_with_options({"_id": {"$in": tags_query}})
        if len(tags) != len(req.tags):
            raise ExceptionHandler(code=ErrorCodes.NOT_FOUND, msg="Some tags not found")

        author = await self.account_repository.find_one(
            {"_id": ObjectId(req.author_id)}
        )
        if not author:
            raise ExceptionHandler(code=ErrorCodes.NOT_FOUND, msg="Author not found")

        problem = await self.problem_repository.find_one({"title": req.title})
        if problem:
            raise ExceptionHandler(
                code=ErrorCodes.CONFLICT, msg="Problem already exists"
            )

        entity = ProblemEntity.new(
            author_id=req.author_id,
            title=req.title,
            description=req.description,
            input=req.input,
            output=req.output,
            source=req.source,
            time_limit=req.time_limit,
            memory_limit=req.memory_limit,
            sample_input=req.sample_input,
            sample_output=req.sample_output,
            real_input=req.real_input,
            real_output=req.real_output,
            note=req.note,
            tags=req.tags,
            io_mode=req.io_mode,
            level=req.level,
        )

        return await self.problem_repository.create(entity)

    async def update_problem(self, id: string, req: UpdateProblemReq) -> ProblemEntity:
        if not ObjectId.is_valid(id):
            raise ExceptionHandler(
                code=ErrorCodes.BAD_REQUEST, msg="Please provide a valid problem ID"
            )

        problem = await self.problem_repository.find_one({"_id": ObjectId(id)})
        if not problem:
            raise ExceptionHandler(code=ErrorCodes.NOT_FOUND, msg="Problem not found")

        response = await self.problem_repository.update(id, req.dict())
        if not response:
            raise ExceptionHandler(
                code=ErrorCodes.INTERNAL_SERVER_ERROR, msg="Failed to update problem"
            )

        return response

    async def find_problems(
        self, query: FindProblemsQuery
    ) -> Tuple[List[ProblemAggregate], Meta]:
        response = await self.problem_repository.find_problems_pagination(query)
        return response

    async def find_problem(self, id: string) -> ProblemAggregateDetail:
        if not ObjectId.is_valid(id):
            raise ExceptionHandler(
                code=ErrorCodes.BAD_REQUEST, msg="Please provide a valid problem ID"
            )

        problem = await self.problem_repository.find_problem(id)
        if not problem:
            raise ExceptionHandler(code=ErrorCodes.NOT_FOUND, msg="Problem not found")

        return problem

    async def delete_problem(self, id: string) -> ProblemEntity:
        if not ObjectId.is_valid(id):
            raise ExceptionHandler(
                code=ErrorCodes.BAD_REQUEST, msg="Please provide a valid problem ID"
            )

        problem = await self.problem_repository.delete(id)
        if not problem:
            raise ExceptionHandler(code=ErrorCodes.NOT_FOUND, msg="Problem not found")

        return problem

    async def fake(self, req: CreateProblemReq):
        problems = await self.problem_repository.find_with_options({})
        if len(problems) > 1000:
            raise ExceptionHandler(code=ErrorCodes.BAD_REQUEST, msg="Too many problems")

        tags = await self.tag_repository.find_with_options({})
        authors = await self.account_repository.find_with_options({})

        count = 0
        names = [
            "Count Island",
            "Move in Matrix",
            "Count Connected Components",
            "Find First Missing Positive",
            "Count Substrings",
            "Find First Unique Character",
            "Find First Non-Repeating Character",
        ]

        for i in range(5):
            # pick a random author
            author_random = random.choice(authors)
            if not author_random:
                continue
            author_id = str(author_random.id)

            # pick some tags
            tags_id = [
                tag.id
                for tag in random.sample(tags, random.randint(1, 5))
                if tag and tag.id
            ]
            if not tags_id:
                continue

            # pick a level
            level = random.choice(
                [
                    ProblemLevel.BEGINNER,
                    ProblemLevel.EASY,
                    ProblemLevel.MEDIUM,
                    ProblemLevel.HARD,
                ]
            )

            # pick a io mode
            io_mode = random.choice([IOMode.STANDARD_IO, IOMode.FILE_IO])

            # pick a name
            name = random.choice(names)

            entity = ProblemEntity.new(
                author_id=author_id,
                title=name,
                description=req.description,
                input=req.input,
                output=req.output,
                source=req.source,
                time_limit=req.time_limit,
                memory_limit=req.memory_limit,
                sample_input=req.sample_input,
                sample_output=req.sample_output,
                real_input=req.real_input,
                real_output=req.real_output,
                note=req.note,
                tags=tags_id,
                io_mode=io_mode,
                level=level,
            )

            response = await self.problem_repository.create_problem(entity)
            print(response)
            count += 1

        print(f"Total problems created: {count}")
