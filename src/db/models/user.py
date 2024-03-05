"""User model file."""
import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class User(Base):
    """User model."""

    user_id: Mapped[int] = mapped_column(
        sa.BigInteger, unique=True, nullable=False
    )
    """ Telegram user id """
    user_name: Mapped[str] = mapped_column(
        sa.Text, unique=False, nullable=True
    )
    """ Telegram user name """
    full_name: Mapped[str] = mapped_column(
        sa.Text, unique=False, nullable=True
    )
    """ Telegram full name """
    phone_number: Mapped[str] = mapped_column(
        sa.Text, unique=False, nullable=True
    )
