from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from src.bot.structures.text.text import info_more_btn_text

info_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text=info_more_btn_text, callback_data='info_more'
            )
        ]
    ]
)
