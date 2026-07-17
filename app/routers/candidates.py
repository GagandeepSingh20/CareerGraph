from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import CandidateDB
from app.schemas import CandidateCreate, CandidateResponse


router = APIRouter(
    prefix="/candidates",
    tags=["Candidates"],
)


@router.post(
    "/",
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


@router.get(
    "/",
    response_model=list[CandidateResponse],
)
def candidates_list(
    db: Annotated[Session, Depends(get_db)],
):
    statement = select(CandidateDB)
    candidates = db.scalars(statement).all()

    return candidates


@router.get(
    "/{candidate_id}",
    response_model=CandidateResponse,
)
def candidate_data(
    candidate_id: int,
    db: Annotated[Session, Depends(get_db)],
):
    statement = select(CandidateDB).where(CandidateDB.id == candidate_id)
    candidate = db.scalar(statement)

    if candidate is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Candidate not found",
        )

    return candidate