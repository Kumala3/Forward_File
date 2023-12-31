from aiogram.dispatcher.filters.state import StatesGroup, State


class UserData(StatesGroup):
    user_id_select = State()
    username_select = State()
    full_name_select = State()
    lang_code_select = State()
    is_premium_select = State()
    registered_time_select = State()
    all_data = State()
