import uuid
from typing import Optional

from sqlalchemy import UUID, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .db import Base


class User(Base):
    first_name: Mapped[str]
    last_name: Mapped[Optional[str]]
    email: Mapped[str]
    password: Mapped[str]
    role_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("role.id")
    )
    role: Mapped["Role"] = relationship(back_populates="user")


class Role(Base):
    role_name: Mapped[str] = mapped_column(String(150), unique=True)
    user: Mapped["User"] = relationship(back_populates="role")
