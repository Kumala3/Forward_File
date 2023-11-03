import asyncio

from aiogram import Dispatcher, Bot
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from aiogram.types import Message

from tgbot.filters.admin import AdminFilter
from tgbot.keyboards.admin_funcs import admin_keyboard
from tgbot.misc.allow_access import allow_access
from tgbot.misc.id_state import Test
from tgbot.services.db_api import DataBase
from tgbot.texts.delete_user import warning_message, question_1, cancel_text
# from tgbot.misc.throttling import rate_limit
from tgbot.texts.greeting_admin import admin_instructions
from tgbot.texts.unregonised_message import unregistered_message


def register_admin(dp: Dispatcher, bot: Bot):
    db = DataBase()

    @allow_access(True)
    # @rate_limit(30, key="admin_start", num_messages=5)
    @dp.message_handler(AdminFilter(is_admin=True), commands=['start'])
    async def admin_start(message: Message):
        await message.answer(text=admin_instructions, reply_markup=admin_keyboard)

    @dp.message_handler(AdminFilter(is_admin=True))
    async def unrecognised_command(message: Message):
        await message.answer(text=unregistered_message)

    @dp.callback_query_handler(text="delete_user", state=None)
    async def state_user(call: CallbackQuery):
        await call.message.answer(text=warning_message)
        await Test.admin_choice.set()

    @dp.message_handler(state=Test.admin_choice)
    async def check_admin_choice(message: Message, state: FSMContext):
        choice_admin = message.text

        await state.update_data(admin_choice=choice_admin)
        if str(choice_admin).lower() == "yes":
            await message.answer(text=question_1)
            await Test.state_user_id.set()
        else:
            sent_message = await message.answer(
                text=cancel_text)
            await state.set_state(None)
            await asyncio.sleep(3)
            await bot.delete_message(chat_id=sent_message.chat.id, message_id=sent_message.message_id)
            await message.answer(text=admin_instructions, reply_markup=admin_keyboard)

    @dp.message_handler(state=Test.state_user_id)
    async def block(message: Message, state: FSMContext):

        admin_answer = message.text
        await state.update_data(answer1=admin_answer)
        await state.set_state(None)

        deleted_user = db.select_username(int(admin_answer))

        db.delete_user(int(admin_answer))
        await message.answer(f"You successful delete user: @{str(deleted_user[0])}")

    @dp.callback_query_handler(text="quantity_users")
    async def quantity_users(call: CallbackQuery):
        count_user = db.count_users()
        await call.message.answer(text=f"Number users: {count_user[0]}")

    # @dp.callback_query_handler(text="info_user")
    # async def info_user(call: CallbackQuery):
    #     users_info = db.select_user()

