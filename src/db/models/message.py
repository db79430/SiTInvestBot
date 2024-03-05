"""Channel model file."""

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .user import User
from .chat import Chat
from .base import Base


class Message(Base):
    """Channel model."""

    message_text: Mapped[str]
    message_id: Mapped[int]
    chat_fk = mapped_column(sa.ForeignKey('chat.id', ondelete='CASCADE'))
    user_fk = mapped_column(sa.ForeignKey('user.id'))
    user_fullname = mapped_column(sa.ForeignKey('user.fullname'))
    user_phone = mapped_column(sa.ForeignKey('user.phone'))
    chat = relationship(
        Chat,
        uselist=False,
        back_populates='chat_messages',
        cascade='save-update,delete',
        lazy='joined',
    )

    message_username: Mapped[User] = relationship(
        uselist=False,
        secondary='User',
        back_populates='chat_messages',
        cascade='save-update',
        lazy='select',
    )
    message_phone: Mapped[User] = relationship(
        uselist=True,
        secondary='User',
        cascade='save-update, delete, delete-orphan',
        lazy='select',
    )
