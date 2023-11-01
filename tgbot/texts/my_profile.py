from aiogram.utils.markdown import hbold


def show_start_text(username: str):
    greeting_text = "\n".join(
        [
            f"{hbold(f'Welcome {username} !')}",
        ]
    )
    return greeting_text
