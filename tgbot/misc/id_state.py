from aiogram.dispatcher.filters.state import StatesGroup, State


class Test(StatesGroup):
    state_user_id = State()
    admin_choice = State()