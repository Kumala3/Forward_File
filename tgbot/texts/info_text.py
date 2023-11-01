from aiogram.utils.markdown import hbold
from tgbot.config import load_config


def show_info(sup_username):
    text_info = "\n".join(
        [
            f"{hbold(f'Bot information')}",
            "You can only send files up to 20mb (Telegram restrictions)",
            f"❤️ Any questions left - {sup_username}",
        ]
    )
    return text_info
