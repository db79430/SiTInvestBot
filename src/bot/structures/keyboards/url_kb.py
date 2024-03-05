from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def build_url_kb() -> InlineKeyboardMarkup:
    review_btn = InlineKeyboardButton(
        text='📺 Видео отзыв о закрытии сделки',
        url='https://drive.google.com/drive/folders/19IeOJkH9da5QkC73dUInJsBCj-rOc6pq',
    )
    present_btn = InlineKeyboardButton(
        text='📌 Презентация и видео застройщика',
        url='https://drive.google.com/drive/folders/19IeOJkH9da5QkC73dUInJsBCj-rOc6pq',
    )
    rows = [[review_btn], [present_btn]]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    return markup


def build_trans_kb() -> InlineKeyboardMarkup:
    trans_btn = InlineKeyboardButton(
        text='🏙 Подробнее о траншевая ипотекаи',
        url='https://blog.domclick.ru/home/post/ipoteka-transhami-kak-rabotaet-transhevaya-ipoteka-v-sbere-i'
        '-pochemu-eto-vygodno',
    )
    row = [[trans_btn]]
    markup = InlineKeyboardMarkup(inline_keyboard=row)
    return markup


def build_credit_kb() -> InlineKeyboardMarkup:
    credit_btn = InlineKeyboardButton(
        text='✅ Акредитация Застройщика банком',
        url='https://blog.domclick.ru/nedvizhimost/post/novostrojka-akkreditovana-chto-eto-znachit-dlya-pokupatelya'
        '-kvartiry',
    )
    row = [[credit_btn]]
    markup = InlineKeyboardMarkup(inline_keyboard=row)
    return markup
