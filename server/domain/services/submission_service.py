from bson import ObjectId
from typing import List, Tuple
from fastapi import Depends
import judge0

from server.core.types import string
from server.core.https import Meta
from server.domain.entities.submission_entity import (
    SubmissionEntity,
    SubmissionLanguages,
    SubmissionStatus,
)
from server.domain.repositories.account_repository import AccountRepository
from server.domain.repositories.problem_repository import ProblemRepository
from server.domain.repositories.submission_repository import SubmissionRepository
from server.domain.usecases.submission_usecases import (
    CreateSubmissionReq,
    FindSubmissionsQuery,
    ManageSubmissionUseCases,
    GradingSubmissionUseCase,
    GradingSubmissionReq,
)
from server.core.exceptions import ErrorCodes, ExceptionHandler
from server.domain.aggregates.problem_aggregate import ProblemBase
from server.domain.entities.account_entity import AccountEntity


class SubmissionService(ManageSubmissionUseCases, GradingSubmissionUseCase):
    def __init__(
        self,
        submission_repository: SubmissionRepository = Depends(),
        problem_repository: ProblemRepository = Depends(),
        account_repository: AccountRepository = Depends(),
    ):
        self.submission_repository = submission_repository
        self.problem_repository = problem_repository
        self.account_repository = account_repository

    # ================================ Common Functions ===================================
    async def _validate(
        self, author_id: string, problem_id: string, language: int
    ) -> Tuple[AccountEntity, ProblemBase]:
        # validate data
        if not ObjectId.is_valid(author_id):
            raise ExceptionHandler(
                code=ErrorCodes.BAD_REQUEST, msg="Please provide a valid author ID."
            )

        if not ObjectId.is_valid(problem_id):
            raise ExceptionHandler(
                code=ErrorCodes.BAD_REQUEST, msg="Please provide a valid problem ID."
            )

        if language not in SubmissionLanguages:
            raise ExceptionHandler(
                code=ErrorCodes.BAD_REQUEST, msg="Please provide a valid language."
            )

        # validate database
        account = await self.account_repository.find_one({"_id": ObjectId(author_id)})
        if not account:
            raise ExceptionHandler(code=ErrorCodes.NOT_FOUND, msg="Account not found.")

        problem = await self.problem_repository.find_base(problem_id)
        if not problem:
            raise ExceptionHandler(code=ErrorCodes.NOT_FOUND, msg="Problem not found.")

        return account, problem

    # ================================ Manage Submission ===================================
    async def create_submission(self, req: CreateSubmissionReq) -> SubmissionEntity:
        account, problem = await self._validate(
            req.author_id, req.problem_id, req.language
        )

        entity = SubmissionEntity.create(
            author_id=req.author_id,
            problem_id=req.problem_id,
            author_name=account.username,
            source_code=req.source_code,
            title=problem.title,
            time_limit=problem.time_limit,
            memory_limit=problem.memory_limit,
            status=SubmissionStatus.SUBMITTED,
            language=SubmissionLanguages.CPP,
            memory=0,
            time=0,
        )

        return await self.submission_repository.create_submission(entity)

    async def find_submissions(
        self, req: FindSubmissionsQuery
    ) -> Tuple[List[SubmissionEntity], Meta]:
        return [], Meta.empty()

    # ================================ Grading Submission ===================================
    async def grading_submission(self, req: GradingSubmissionReq) -> SubmissionEntity:
        account, problem = await self._validate(
            req.author_id, req.problem_id, req.language
        )

        # start grading here
        judge0_submission = judge0.Submission(
            source_code=req.source_code,
            language=req.language.to_language_alias(),
        )

        response = judge0.run(
            submissions=judge0_submission,
        )
        print("Judge0 Response: ", response.stdout)

        entity = SubmissionEntity.create(
            author_id=req.author_id,
            problem_id=req.problem_id,
            author_name=account.username,
            source_code=req.source_code,
            title=problem.title,
            time_limit=problem.time_limit,
            memory_limit=problem.memory_limit,
            status=SubmissionStatus.SUBMITTED,
            language=req.language,
            memory=0,
            time=0,
        )

        return entity
