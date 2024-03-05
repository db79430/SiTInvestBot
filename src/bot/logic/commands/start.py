"""This file represents a start logic."""

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from src.bot.filters.register_filter import RegisterFilter

from src.bot.structures.keyboards.menu_btn import menu_btn
from src.bot.structures.keyboards.registration_kb import register_kb

start_router = Router(name='start')


@start_router.message(CommandStart(), RegisterFilter())
async def start_wo_register(message: Message):
    await message.answer(
        text=f'Привет, {message.from_user.full_name} 👋!'
        f'\n На связи бот и команда SiTInvest.'
        f'\n 🏘Мы занимаемся инвестициями в сфере строительства.\n'
        f'\n 🤖В этом боте ты получишь подробную информацию, что такое инвестирование в стройку и сможешь '
        f'начать зарабатывать на строительстве'
        f"\n Нажми на кнопку внизу 'регистрация', чтобы начать сотрудничать с нами 😊\n",
        reply_markup=register_kb,
    )


@start_router.message(CommandStart())
async def start_w_register(message: Message):
    markup = menu_btn()
    return await message.answer('Меню', reply_markup=markup)
