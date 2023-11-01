from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

cancel_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Cancel", callback_data="Cancel_send_file"),
        ],

    ]
)
