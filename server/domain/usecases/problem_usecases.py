from abc import ABC, abstractmethod
from typing import List, Tuple

from fastapi_camelcase import CamelModel
from server.core.https import BaseQuery, Meta
from server.core.types import string
from server.domain.aggregates.problem_aggregate import ProblemAggregate
from server.domain.entities.problem_entity import IOMode, ProblemLevel
from server.domain.entities.problem_entity import ProblemEntity
from server.domain.aggregates.problem_aggregate import ProblemAggregateDetail

class CreateProblemReq(CamelModel):
    author_id: string
    title: string
    description: string
    input: string
    output: string
    time_limit: int
    memory_limit: int
    sample_input: string
    sample_output: string
    real_input: string
    real_output: string
    tags: List[string]
    note: string = ""
    source: string = ""
    io_mode: IOMode = IOMode.STANDARD_IO
    level: ProblemLevel = ProblemLevel.BEGINNER

class UpdateProblemReq(CamelModel):
    title: string
    description: string
    input: string
    output: string
    time_limit: int
    memory_limit: int
    sample_input: string
    sample_output: string
    real_input: string
    real_output: string
    tags: List[string]
    note: string = ""
    source: string = ""
    io_mode: IOMode = IOMode.STANDARD_IO
    level: ProblemLevel = ProblemLevel.BEGINNER

class FindProblemsQuery(BaseQuery):
    levels: List[ProblemLevel] = []
    tags: List[string] = []

class ManageProblemUseCases(ABC):
    @abstractmethod
    async def create_problem(self, req: CreateProblemReq) -> ProblemEntity: ...

    @abstractmethod
    async def update_problem(self, id: string, req: UpdateProblemReq) -> ProblemEntity: ...

    @abstractmethod
    async def find_problems(self, query: FindProblemsQuery) -> Tuple[List[ProblemAggregate], Meta]: ...

    @abstractmethod
    async def find_problem(self, id: string) -> ProblemAggregateDetail: ...

    @abstractmethod
    async def delete_problem(self, id: string) -> ProblemEntity: ...
