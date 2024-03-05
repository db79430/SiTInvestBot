from aiogram.filters import BaseFilter


class RegisterFilter(BaseFilter):
    async def __call__(self, *args, **kwargs):
        # Get information from the database
        return True
