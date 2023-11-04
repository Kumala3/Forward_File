from aiogram.dispatcher.filters.state import StatesGroup, State


class UserState(StatesGroup):
    user_id = State()
    admin_choice = State()
    user_idd = State()