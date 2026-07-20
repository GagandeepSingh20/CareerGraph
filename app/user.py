from datetime import datetime, timezone

from sqlalchemy import DateTime, Float, Integer, String, Boolean, JSON
from sqlalchemy.orm import Mapped, mapped_column

from .database import Base

def current_utc_time() -> datetime:
    return datetime.now(timezone.utc)


class UserDB(Base):

    __tablename__ = "users"

    id: Mapped [int] = mapped_column(
        Integer,
        primary_key= True,
        index = True,
    )

    email: Mapped[str] = mapped_column(
        String,
        unique = True,
        index = True,
        nullable = False,
    )

    hashed_password: Mapped[str] = mapped_column(
        String,
        index = True,
        nullable = False,
    )

    role: Mapped[str] = mapped_column(
        String,
        nullable = False,
    )

    created_at: Mapped[DateTime] = mapped_column(
        DateTime,
        nullable= False
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable= False
    )
