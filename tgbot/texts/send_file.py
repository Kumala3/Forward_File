from aiogram.utils.markdown import hbold

file_send_rules_notifier = "\n".join(
    [
        f"{hbold('1) By submitting files you agree to the rules of using the bot')}",
        f"{hbold('2) Send a .zip or .rar file up to 20mb (Telegram limitation) или же отправьте ссылку на файл')}",


    ]
)
