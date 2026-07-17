from fastapi import FastAPI, Depends, HTTPException, status

from typing import Annotated
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from .database import Base, engine, get_db
from .models import CandidateDB, JobDB
from .schemas import CandidateCreate, CandidateResponse, JobCreate, JobResponse

Base.metadata.create_all(bind=engine)

app=FastAPI(
    title="CareerGraph API",
    description="Candidate and job matching backend",
)

# HTTP requests

@app.get("/")
def welcome():
  return {"message":"Welcome to Career Graph"}

@app.get("/health")
def health_check():
    return {"status":"Server is running in okay condition"}

# Candidate related HTTP requests
@app.post(
    "/candidates/",
    response_model=CandidateResponse,
    status_code=status.HTTP_201_CREATED,
)
def candidate_creation(
    candidate: CandidateCreate,
    db: Annotated[Session, Depends(get_db)],
):
    existing_email = db.scalar(
        select(CandidateDB.id).where(
            CandidateDB.email == str(candidate.email)
        )
    )

    if existing_email is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A candidate with this email already exists",
        )

    if candidate.linkedin_url is not None:
        existing_linkedin = db.scalar(
            select(CandidateDB.id).where(
                CandidateDB.linkedin_url == str(candidate.linkedin_url)
            )
        )

        if existing_linkedin is not None:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="A candidate with this LinkedIn profile already exists",
            )

    candidate_data = candidate.model_dump(mode="json")
    database_candidate = CandidateDB(**candidate_data)

    try:
        db.add(database_candidate)
        db.commit()
        db.refresh(database_candidate)

    except IntegrityError:
        db.rollback()

        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Candidate already exists",
        )

    return database_candidate


@app.get("/candidates",
        response_model=list[CandidateResponse],)
def candidates_list(db: Annotated[Session, Depends(get_db)],):
    statement = select(CandidateDB)
    candidates = db.scalars(statement).all()

    return candidates

@app.get("/candidates/{candidate_id}",
        response_model=CandidateResponse,)
def candidate_data(candidate_id: int,
                   db: Annotated[Session, Depends(get_db)],):
    statement = select(CandidateDB).where(CandidateDB.id == candidate_id)
    candidate = db.scalar(statement)

    if candidate is None:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail="Candidate not found",
        )

    return candidate

# Job related HTTP requests

@app.post(
    "/jobs/",
    response_model=JobResponse,
    status_code=status.HTTP_201_CREATED,)
def job_creation(
    job:JobCreate,
    db: Annotated[Session, Depends(get_db)],
):
    
    existing_job= db.scalar(
        select(JobDB.id).where(
            JobDB.title == str(job.title),
            JobDB.company == str(job.company),
            JobDB.location == str(job.location),
        )
    )

    if existing_job is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="This Job already exists",
        )

    job_data = job.model_dump(mode="json")
    database_job =JobDB(**job_data)

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

@app.get("/jobs",
         response_model=list[JobResponse],
    )
def job_list(db: Annotated[Session, Depends(get_db)]):
    statement = select(JobDB)
    jobs = db.scalars(statement).all()

    return jobs

@app.get("/jobs/{job_id}",
         response_model=JobResponse,)
def job_data(job_id: int,
              db: Annotated[Session, Depends(get_db)]
):
    statement = select(JobDB).where(JobDB.id == job_id)
    job = db.scalar(statement)

    if job is None:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail="Job not found",
        )

    return job