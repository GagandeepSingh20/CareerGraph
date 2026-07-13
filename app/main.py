from fastapi import FastAPI, Depends, HTTPException, status

from typing import Annotated
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from .database import Base, engine, get_db
from .models import CandidateDB
from .schemas import CandidateCreate, CandidateResponse

Base.metadata.create_all(bind=engine)

app=FastAPI(
    title="CareerGraph API",
    description="Candidate and job matching backend",
)


@app.get("/")
def welcome():
  return {"message":"Welcome to Career Graph"}

@app.get("/health")
def health_check():
    return {"status":"Server is running in okay condition"}

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
