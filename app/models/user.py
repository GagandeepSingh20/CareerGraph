from datetime import datetime, timezone

from sqlalchemy import DateTime, Float, Integer, String, Boolean, JSON
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base
from .utils import current_utc_time


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
        nullable = False,
    )

    role: Mapped[str] = mapped_column(
        String,
        nullable = False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default= current_utc_time,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default= True,
        nullable= False,
    )
