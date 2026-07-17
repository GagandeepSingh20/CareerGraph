from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import JobDB
from app.schemas import JobCreate, JobResponse


router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"],
)


@router.post(
    "/",
    response_model=JobResponse,
    status_code=status.HTTP_201_CREATED,
)
def job_creation(
    job: JobCreate,
    db: Annotated[Session, Depends(get_db)],
):
    existing_job = db.scalar(
        select(JobDB.id).where(
            JobDB.title == job.title,
            JobDB.company == job.company,
            JobDB.location == job.location,
        )
    )

    if existing_job is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="This job already exists",
        )

    job_data = job.model_dump(mode="json")
    database_job = JobDB(**job_data)

    try:
        db.add(database_job)
        db.commit()
        db.refresh(database_job)

    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Job already exists",
        )

    return database_job


@router.get(
    "/",
    response_model=list[JobResponse],
)
def jobs_list(
    db: Annotated[Session, Depends(get_db)],
):
    statement = select(JobDB)
    jobs = db.scalars(statement).all()

    return jobs


@router.get(
    "/{job_id}",
    response_model=JobResponse,
)
def job_data(
    job_id: int,
    db: Annotated[Session, Depends(get_db)],
):
    statement = select(JobDB).where(JobDB.id == job_id)
    job = db.scalar(statement)

    if job is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job not found",
        )

    return job