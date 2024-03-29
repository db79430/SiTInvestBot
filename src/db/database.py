"""Database class with all-in-one features."""

from sqlalchemy.engine.url import URL
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine as _create_async_engine

from src.configuration import conf

from .repositories import ChatRepo, MessageRepo, UserRepo


def create_async_engine(url: URL | str) -> AsyncEngine:
    """Create async engine with given URL.

    :param url: URL to connect
    :return: AsyncEngine
    """
    return _create_async_engine(url = url, echo = conf.debug, pool_pre_ping = True)

print(conf.db.build_connection_str())
class Database:
    """Database class.

    is the highest abstraction level of database and
    can be used in the handlers or any others bot-side functions.
    """

    user: UserRepo
    """ User repository """
    chat: ChatRepo
    """ Chat repository """
    message: MessageRepo
    """ Message repository """

    session: AsyncSession

    def __init__(
            self,
            session: AsyncSession,
            user: UserRepo = None,
            chat: ChatRepo = None,
            message: MessageRepo = None,
    ):
        """Initialize Database class.

        :param session: AsyncSession to use
        :param user: (Optional) User repository
        :param chat: (Optional) Chat repository
        """
        self.session = session
        self.user = user or UserRepo(session = session)
        self.chat = chat or ChatRepo(session = session)
        self.message = message or MessageRepo(session = session)
