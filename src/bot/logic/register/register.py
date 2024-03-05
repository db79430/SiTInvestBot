import re

from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from src.bot.structures.fsm.register import (
    RegisterGroup,)
from ...structures.keyboards.info_kb import info_kb
from ...structures.keyboards.menu_btn import menu_btn
from .router import register_router
from src.configuration import conf



@register_router.callback_query(F.data == 'register')
async def register_confirmation(call: CallbackQuery, state: FSMContext):
    await state.set_state(RegisterGroup.regFullName)
    return await call.message.answer(' 📝Введите ваше ФИО на русском языке:')


@register_router.message(RegisterGroup.regFullName)
async def register_full_name(message: Message, state: FSMContext):
    await state.clear()
    if re.findall('^[а-яА-Я ]+$', message.text):
        await message.reply(
            'Супер 🙂! Имя я зарегистрировал\n'
            ' 📱Теперь нужно ввести номер телефона (+7xxxxxxxxx):\n'
        )
        await state.update_data(regFullName=message.text)
        await state.set_state(RegisterGroup.regPhone)
    else:
        await message.reply('Неккоректное имя')


@register_router.message(RegisterGroup.regPhone)
async def register_phone(message: Message, state: FSMContext):
    if re.findall(
        '^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$', message.text
    ):
        await state.update_data(regPhone=message.text)
        await state.clear()
        reg_data = await state.get_data()
        reg_name = reg_data.get(RegisterGroup.regFullName)
        reg_phone = reg_data.get(RegisterGroup.regPhone)
        msg = (
            f'✅ Вы успешно зарегистрированы!\n'
            f'📝 ФИО: {reg_name}\n'
            f'📱 Телефон: {reg_phone}\n'
            f'Мы сохранили Вашу информацию и скоро свяжемся с Вами.'
        )
        await message.answer(text=msg, reply_markup=info_kb)

        await message.reply_markup(menu_btn)
    else:
        await message.answer('Некорректный телефон')


@register_router.message(RegisterGroup.regFullName, RegisterGroup.regPhone)
async def send_message(message: Message, state: FSMContext):
    data = await state.get_data()
    await message.reply_to_message(conf.bot.chat, data=data, positive=False)
