from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

admin_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Block_User", callback_data="block_user"),
            InlineKeyboardButton(text="UnBlock_User", callback_data="unblock_user"),
            InlineKeyboardButton(text="Delete_user", callback_data="delete_user"),
            # InlineKeyboardButton(text="Quantity_Users", callback_data="quantity_users"),
            InlineKeyboardButton(text="Info_User", callback_data="info_user"),
        ],
        [
            InlineKeyboardButton(text="Quantity_Users", callback_data="quantity_users"),

        ]

    ],
)
