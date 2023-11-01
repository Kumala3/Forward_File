from aiogram.utils.markdown import hbold


def get_bot_rules(sup_username):
    rules = "\n".join(
        [
            f"{hbold(f'Bot rules')}",
            "You can only send files up to 20mb (Telegram restrictions)",
            f"❤️ Any questions left - {sup_username}",
        ]
    )
    return rules
