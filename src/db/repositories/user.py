"""User repository file."""

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import InstrumentedAttribute

from ..models.user import User
from .abstract import Repository


class UserRepo(Repository[User]):
    """User repository for CRUD and other SQL queries."""

    def __init__(self, session: AsyncSession):
        """Initialize user repository as for all users or only for one user."""
        super().__init__(type_model = User, session = session)

    async def new(
            self,
            user_id: int,
            user_name: str = None,
            full_name: str = None,
            phone_number: str = None,
    ) -> User:
        """Insert a new user into the database
        :param user_id: Telegram user id
        :param user_name: Telegram username
        :param full_name: Telegram profile first name
        :param phone_number: Telegram phone user.

        """
        new_user = await self.session.merge(
            User(
                user_id = user_id,
                user_name = user_name,
                full_name = full_name,
                phone_number = phone_number,
            )
        )
        print("new_user", new_user)
        return new_user



