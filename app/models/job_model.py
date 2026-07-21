from datetime import datetime, timezone

from sqlalchemy import DateTime, Float, Integer, String, Boolean, JSON
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base
from .utils import current_utc_time

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
