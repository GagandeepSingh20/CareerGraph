from datetime import datetime, timezone

from sqlalchemy import DateTime, Float, Integer, JSON, String
from sqlalchemy.orm import Mapped, mapped_column

from .database import Base

def current_utc_time() -> datetime:
    return datetime.now(timezone.utc)

# Candidate database model

class CandidateDB(Base):

    __tablename__ = "candidates"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key = True,
        index = True,
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable = False,
    )

    age: Mapped[int] = mapped_column(
        Integer,
        nullable = False,
    )

    cgpa: Mapped[float] = mapped_column(
        Float,
        nullable = False,
    )

    gender: Mapped[str] = mapped_column(
        String,
        nullable = False,
    )

    email: Mapped[str] = mapped_column(
        String,
        unique = True,
        index = True,
        nullable = False,
    )

    linkedin_url: Mapped[str | None] = mapped_column(
        String,
        unique=True,
        nullable = True,
    )

    skills: Mapped[list[str] | None] = mapped_column(
        JSON,
        nullable=True,
    )

    experience: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    graduation_year: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=current_utc_time,
        nullable=False,
    )

# Job database model

class JobDB(Base):
     
    __tablename__ = "jobs"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key = True,
        index = True,
    )

    title: Mapped[str] = mapped_column(
        String(100),
        nullable = False,
    )

    company: Mapped[str] = mapped_column(
        String(200),
        nullable = False,
    )

    required_skills: Mapped[list[str]] = mapped_column(
        JSON,
        nullable=False,
    )

    min_experience: Mapped[int] = mapped_column(
        Integer,
        nullable = False,
    )

    location: Mapped[str] = mapped_column(
        String(200),
        nullable = False,
    )

    job_type: Mapped[str] = mapped_column(
        String,
        nullable = False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=current_utc_time,
        nullable=False,
    )
