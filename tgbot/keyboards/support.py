from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def create_support_keyboard(sup_username: str):
    sup_user = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Technically support", url=f"https://t.me/{sup_username[1:]}")
            ]
        ]
    )
    return sup_user
