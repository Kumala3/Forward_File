from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.types import CallbackQuery
from aiogram.types import Message

from tgbot.config import load_config
from tgbot.keyboards.cancel_file import cancel_keyboard
from tgbot.keyboards.start_panel import keyboard_panel
from tgbot.keyboards.support import create_support_keyboard
from tgbot.texts.bot_rules import get_bot_rules
from tgbot.texts.greeting_user import get_welcome_text
from tgbot.texts.send_file import rules_sending_file
from tgbot.texts.user_profile import get_user_info


def register_user_panel(dp: Dispatcher):
    support_username = load_config().tg_bot.support_username

    @dp.message_handler(commands=['start'])
    async def user_start(message: Message):
        username = message.from_user.username
        await message.answer(text=get_welcome_text(username), reply_markup=keyboard_panel)

    @dp.message_handler(text="My profile")
    async def cancel_sending_file(message: Message):
        user_id = message.from_user.id
        username = message.from_user.username
        await message.answer(text=get_user_info(user_id, username))

    @dp.message_handler(text="Information")
    async def info(message: Message):
        await message.answer(text=get_bot_rules(support_username), reply_markup=create_support_keyboard(support_username))

    @dp.message_handler(text="Send file")
    async def send_file(message: Message):
        await message.answer(text=rules_sending_file, reply_markup=cancel_keyboard)

    @dp.message_handler(content_types=types.ContentType.DOCUMENT)
    async def get_file(message: Message):
        config = load_config()
        file_name = message.document.file_name
        if file_name.endswith(('.zip', '.rar')):
            await message.forward(config.tg_bot.channel_username)
            await message.reply(text="Your file successfully send!Wait for a message from admin!")
        else:
            await message.reply("Please send a file in .zip or .rar format")

    @dp.callback_query_handler(text="Cancel_send_file")
    async def cancel(call: CallbackQuery):
        await call.message.answer(text="File sending cancelled", reply_markup=keyboard_panel)
        await call.message.delete()
