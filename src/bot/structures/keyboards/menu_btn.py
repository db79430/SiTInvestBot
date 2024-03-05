from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from src.bot.structures.text.text import (
    info_more_btn_text,
    invest_without_text_btn,
    invest_with_text_btn,
    partner_text_btn,
)

menu_btn = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=info_more_btn_text, callback_data='info_more')],
        [
            KeyboardButton(
                text=invest_without_text_btn, callback_data='invest_without'
            )
        ],
        [
            KeyboardButton(
                text=invest_with_text_btn, callback_data='invest_with'
            )
        ],
        [KeyboardButton(text=partner_text_btn, callback_data='partner_with')],
    ],
    resize_keyboard=True,
    resize_horizontal=True,
)
