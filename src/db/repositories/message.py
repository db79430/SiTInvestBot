"""Message repository file."""

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from .abstract import Repository
from ..models.chat import Chat
from ..models.message import Message
from ..models.user import User


class MessageRepo(Repository[Message]):
    """Message repository for CRUD and other SQL queries."""

    def __init__(self, session: AsyncSession):
        """Initialize user repository as for all users or only for one user."""
        super().__init__(type_model=Message, session=session)

    async def new(self, message_text: str, message_id: int) -> Message:
        """Insert a new user into the database.
        :param message_id: Telegram message id
        :param message_text: message text.
        """
        new_message = await self.session.merge(
            Message(message_text=message_text, message_id=message_id)
        )
        return new_message


async def get_message_by_fullname(self, message_id: int) -> list[User]:
    """Retrieve message by its ID along with user information."""
    message: Message = await self.session.scalar(
        select(Message)
        .where(Message.message_id == message_id)
        .options(selectinload(Message.user_fullname))
    )
    return message.message_username


async def get_message_by_phone(self, message_id: int) -> list[User]:
    message: Message = await self.session.scalar(
        select(Message)
        .where(Message.message_id == message_id)
        .options(selectinload(Message.message_phone))
        .limit(1)
    )
    return message.message_phone


class RepositoryException:
    pass


async def public_messages(self, message_id, chat: Chat) -> None:
    message: Message = await self.session.scalar(
        select(Message)
        .where(Message.message_id == message_id)
        .options(selectinload(Message.chat))
        .limit(1)
    )
    try:
        message.chat.append(chat)
        await self.session.flush()
    except Exception:
        raise RepositoryException()
