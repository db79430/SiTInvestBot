import asyncio
from aiogram.fsm.context import FSMContext
from aiogram.types import (
    CallbackQuery,
)
from aiogram import F, Router
from src.bot.structures.text.text import (
    invest_without_text,
    invest_with_text,
    invest_benefit_text,
    invest_safety_text,
)
from src.bot.structures.keyboards.url_kb import (
    build_url_kb,
    build_trans_kb,
    build_credit_kb,
)
from src.bot.structures.keyboards.menu_btn import menu_btn

invest_router = Router(name='invest_router')


@invest_router.callback_query(F.data == 'invest_without')
async def invest_without_callback_button(
    callback: CallbackQuery, state: FSMContext
):
    markup = [build_trans_kb(), build_credit_kb(), build_url_kb()]
    await callback.message.answer(
        text=invest_without_text, reply_markup=markup[0]
    )
    await asyncio.sleep(4)
    await callback.message.answer(
        text=invest_benefit_text, reply_markup=markup[1]
    )
    await asyncio.sleep(4)
    await callback.message.answer(
        text=invest_safety_text, reply_markup=markup[2]
    )
    await callback.message.set_reply_markup(reply_markup=menu_btn)


@invest_router.callback_query(F.data == 'invest_with')
async def invest_with_callback_button(
    callback: CallbackQuery, state: FSMContext
):
    await callback.message.answer(text=invest_with_text, show_alert=True)
