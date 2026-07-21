from datetime import datetime, timezone

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base
from .utils import current_utc_time

class RecruiterProfileDB(Base):

    __tablename__ = "recruiter_profiles"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        unique=True,
        nullable=False,
        index=True,
    )

    full_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    organization_name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
        index=True,
    )

    designation: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    organization_website: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    organization_location: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=current_utc_time,
        nullable=False,
    )