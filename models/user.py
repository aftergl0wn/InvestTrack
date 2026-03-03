from typing import Optional

from sqlalchemy.orm import Mapped

from .db import Base


class User(Base):
    first_name: Mapped[str]
    last_name: Mapped[Optional[str]]
    email: Mapped[str]
    password: Mapped[str]
    is_admin: Mapped[bool]
