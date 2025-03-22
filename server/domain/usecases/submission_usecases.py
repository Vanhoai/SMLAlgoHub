from abc import ABC, abstractmethod
from typing import List, Tuple
from server.core.https import BaseQuery, Meta
from server.domain.entities.submission_entity import (
    SubmissionEntity,
    SubmissionLanguages,
)
from fastapi_camelcase import CamelModel
from server.core.types import string

# ================================= Manage Submission ===========================


class CreateSubmissionReq(CamelModel):
    author_id: string
    problem_id: string
    source_code: string
    language: SubmissionLanguages


class FindSubmissionsQuery(BaseQuery):
    pass


class ManageSubmissionUseCases(ABC):
    @abstractmethod
    async def create_submission(self, req: CreateSubmissionReq) -> SubmissionEntity: ...

    @abstractmethod
    async def find_submissions(
        self, req: FindSubmissionsQuery
    ) -> Tuple[List[SubmissionEntity], Meta]: ...


# ================================= Grading Submission ======================================
class GradingSubmissionReq(CamelModel):
    author_id: string
    problem_id: string
    source_code: string
    language: SubmissionLanguages


class GradingSubmissionUseCase(ABC):
    @abstractmethod
    async def grading_submission(
        self, req: GradingSubmissionReq
    ) -> SubmissionEntity: ...
