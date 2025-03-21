from typing import List
from server.domain.entities.account_entity import AccountEntity
from server.domain.entities.base_entity import BaseEntity
from server.core.types import string
from server.domain.entities.tag_entity import TagEntity


class ProblemBase(BaseEntity):
    title: string
    time_limit: int
    memory_limit: int
    io_mode: string
    level: int
    acceptance: float
    sample_input: string
    sample_output: string


class ProblemAggregate(ProblemBase):
    tags: List[TagEntity]


class ProblemAggregateDetail(ProblemAggregate):
    author: AccountEntity
    description: string
    input: string
    output: string
    note: string
    source: string
    real_input: string
    real_output: string
