from fastapi import Depends

from server.domain.services.submission_service import SubmissionService
from server.domain.services.problem_service import ProblemService
from server import dependencies
from server.domain.entities.submission_entity import SubmissionEntity


async def start_grading(
    submission: SubmissionEntity,
    submission_service: SubmissionService = Depends(dependencies.submission_service),
    problem_service: ProblemService = Depends(dependencies.problem_service),
):
    print(submission)
