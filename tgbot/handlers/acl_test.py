from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Command

from tgbot.misc.allow_access import allow_access
from tgbot.models.first_model import User


def register_acl_test(dp: Dispatcher):
    @allow_access(True)
    @dp.message_handler(Command("block_me"))
    async def block_me(message: types.Message, user: User):
        await message.answer(f"The user has a status {user.allowed}. Access is now denied\n"
                             f"To unlock, enter the command /unblock_me")
        user.block()

    @allow_access(True)
    @dp.message_handler(Command("unblock_me"))
    async def unblock_me(message: types.Message, user: User):
        await message.answer(f"Пользователь имеет статус: {user.allowed}. Теперь доступ разрешен\n"
                             f"Чтобы заблокироваться введите команду /block_me")
        user.unblock_me()
