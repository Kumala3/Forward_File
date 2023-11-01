from aiogram import Dispatcher, types

from tgbot.filters.admin import AdminFilter
from tgbot.keyboards.admin_funcs import admin_keyboard
from tgbot.misc.allow_access import allow_access
from tgbot.misc.throttling import rate_limit
from tgbot.texts.greeting_admin import admin_instructions


def register_admin(dp: Dispatcher):
    @allow_access(True)
    @rate_limit(30, key="admin_start", num_messages=5)
    @dp.message_handler(AdminFilter(is_admin=True), commands=['start'])
    async def admin_start(message: types.Message):
        await message.answer(text=admin_instructions, reply_markup=admin_keyboard)
