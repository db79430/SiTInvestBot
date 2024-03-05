from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from src.bot.structures.text.text import (
    invest_with_text_btn,
    invest_without_text_btn,
    partner_text_btn,
)


def build_invest_kb() -> InlineKeyboardMarkup:
    invest_url = InlineKeyboardButton(
        text="Сайт компании застройщика 'Строй и точка' 🌐",
        url='https://xn--80apairckhje0d.xn--p1ai/',
    )
    invest_without_btn = InlineKeyboardButton(
        text=invest_without_text_btn, callback_data='invest_without'
    )
    invest_with_btn = InlineKeyboardButton(
        text=invest_with_text_btn, callback_data='invest_with'
    )
    partner_btn = InlineKeyboardButton(
        text=partner_text_btn, callback_data='partner_with'
    )
    rows = [
        [invest_url],
        [invest_without_btn],
        [invest_with_btn],
        [partner_btn],
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    return markup
