from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard_panel = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="My profile"),
            KeyboardButton(text="Information"),
            KeyboardButton(text="Send file")
        ]
    ],
    resize_keyboard=True
)
