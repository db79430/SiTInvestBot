from aiogram.types import Message

from src.bot.structures.keyboards.menu_btn import menu_btn


async def show_menu(message: Message):
    await message.answer(text='Меню', reply_markup=menu_btn())


async def show_help(message: Message):
    await message.answer(
        'По вопросам работы бота, обратитесь в службу поддержки @....'
    )
