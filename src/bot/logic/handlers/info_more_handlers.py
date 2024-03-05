from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram import Router, F
from src.bot.structures.text.text import info_text
from src.bot.structures.keyboards.invest_kb import build_invest_kb

info_more_router = Router(name='info_more_router')


@info_more_router.callback_query(F.data == 'info_more')
async def callback_info_more(callback: CallbackQuery, state: FSMContext):
    markup = build_invest_kb()
    await callback.answer('')
    await callback.message.answer(text=info_text, reply_markup=markup)
