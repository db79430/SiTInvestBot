from aiogram.filters import CommandObject
from aiogram.fsm.context import FSMContext
from aiogram.types import Message


async def show_help(
    message: Message, command: CommandObject, state: FSMContext
):
    await message.answer(
        text='Если возникли вопросы и проблемы с работой бота, напишите нам @....'
    )
