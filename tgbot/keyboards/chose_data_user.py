from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

data_select_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="User_Id🔴", callback_data="user_id"),
            InlineKeyboardButton(text="Username🔴", callback_data="username"),

        ],
        [
            InlineKeyboardButton(text="Fullname🔴", callback_data="fullname"),
            InlineKeyboardButton(text="Lang_code🔴", callback_data="lang_code"),
        ],
        [
            InlineKeyboardButton(text="Is_premium🔴", callback_data="is_premium"),
            InlineKeyboardButton(text="Registered_time🔴", callback_data="registered_time"),
        ]

    ]

)
