from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from src.bot.structures.text.text import register_btn_text

register_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text=register_btn_text, callback_data='register'
            )
        ]
    ]
)
