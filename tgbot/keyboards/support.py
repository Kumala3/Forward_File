from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def send_support(sup_username: str):
    support_user = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Техническая Поддержка", url=f"https://t.me/{sup_username[1:]}")
            ]
        ]
    )
    return support_user
