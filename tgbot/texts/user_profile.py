from aiogram.utils.markdown import hbold


def get_user_info(user_id: int, username: str):
    user_details = "\n".join(
        [
            f"{hbold(f'Greetings {username}!')}",
            f"{hbold(f'Your id: {user_id}')}\n",

        ]
    )
    return user_details
