from aiogram.utils.markdown import hbold


def get_welcome_text(username: str):
    greetings_text = "\n".join(
        [
            f"{hbold(f'Welcome {username} !')}",
        ]
    )
    return greetings_text
