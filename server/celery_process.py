import asyncio
from celery import Celery
from fastapi import Depends
import multiprocessing
import judge0

from server.domain.entities.submission_entity import SubmissionEntity
from server.domain.services.submission_service import SubmissionService
from server.domain.services.problem_service import ProblemService
import server.dependencies as dependencies

judge_app = Celery(
    "submissions",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
)

judge_app.conf.update(worker_concurrency=multiprocessing.cpu_count())


@judge_app.task(
    name="task.process_submission",
    rate_limit="10/s",
)
async def process_submission(
    submission_id: int,
    # submission_service: SubmissionService = Depends(dependencies.submission_service),
    # problem_service: ProblemService = Depends(dependencies.problem_service),
):
    await asyncio.sleep(5)
    print("Number of cpu : ", multiprocessing.cpu_count())


async def process_submission_async(
    submission_entity: SubmissionEntity,
    submission_service: SubmissionService = Depends(dependencies.submission_service),
    problem_service: ProblemService = Depends(dependencies.problem_service),
):
    await asyncio.sleep(5)
    submission = await problem_service.find_problem(submission_entity.problem_id)
    print("Submission: ", submission.id)
