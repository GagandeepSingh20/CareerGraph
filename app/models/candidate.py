from datetime import datetime, timezone

from sqlalchemy import DateTime, Float, Integer, JSON, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base
from .utils import current_utc_time

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