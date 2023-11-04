from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

data_select_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="User_Id🔴", callback_data="user_id"),
            InlineKeyboardButton(text="Username🔴", callback_data="username"),
        ],
        [
            InlineKeyboardButton(text="Full_name🔴", callback_data="full_name"),
            InlineKeyboardButton(text="Lang_code🔴", callback_data="lang_code"),
        ],
        [
            InlineKeyboardButton(text="💎Is_premium🔴", callback_data="is_premium"),
            InlineKeyboardButton(text="⏳Registered_time🔴", callback_data="registered_time"),
        ],
        [
            InlineKeyboardButton(text="All_data☑️🔴", callback_data="all_data"),
            InlineKeyboardButton(text="Clear_all_data⛔️",
                                 callback_data="clear_all_data")
        ],
        [
            InlineKeyboardButton(text="Finish✅", callback_data="finish")
        ],
    ]
)


async def create_data_select_keyboard(state: FSMContext) -> InlineKeyboardMarkup:
    current_state_data = await state.get_data()

    user_id_state = current_state_data.get('user_id_select', False)
    username_state = current_state_data.get('username_select', False)
    full_name_state = current_state_data.get('full_name_select', False)
    lang_code_state = current_state_data.get("lang_code_select", False)
    is_premium_state = current_state_data.get("is_premium_select", False)
    registered_time_state = current_state_data.get("registered_time_select", False)
    all_data = current_state_data.get("all_data", False)

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=f"User_Id{'🟢' if user_id_state else '🔴'}", callback_data="user_id"),
                InlineKeyboardButton(text=f"Username{'🟢' if username_state else '🔴'}", callback_data="username"),
            ],
            [
                InlineKeyboardButton(text=f"Full_name{'🟢' if full_name_state else '🔴'}", callback_data="full_name"),
                InlineKeyboardButton(text=f"Lang_code{'🟢' if lang_code_state else '🔴'}", callback_data="lang_code"),
            ],
            [
                InlineKeyboardButton(text=f"💎Is_premium{'🟢' if is_premium_state else '🔴'}", callback_data="is_premium"),
                InlineKeyboardButton(text=f"⏳Registered_time{'🟢' if registered_time_state else '🔴'}",
                                     callback_data="registered_time")
            ],
            [
                InlineKeyboardButton(text=f"All_data☑️{'🟢' if all_data else '🔴'}", callback_data="all_data"),
                InlineKeyboardButton(text="Clear_all_data⛔️",
                                     callback_data="clear_all_data")
            ],
            [
                InlineKeyboardButton(text="Finish✅", callback_data="finish")
            ]
        ]
    )
    return keyboard
