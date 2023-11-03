from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_default_commands(bot):
    return await bot.set_my_commands(
        commands=[
            BotCommand("help", "Technically support"),
            BotCommand("information", "Bot rules"),
            BotCommand("send_file", "Send file to bot"),

        ],
        scope=BotCommandScopeDefault()
    )
