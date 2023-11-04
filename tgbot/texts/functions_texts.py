from aiogram.utils.markdown import hbold

warning_message = "\n".join([
    f"{hbold('!!!WARNING!!!')}",
    f"{hbold('Are you sure you want to delete user? (yes/no)')}"

])

user_id_request = hbold("Enter user_id (int) user which you would like to delete")
cancel_text = hbold("Cancel deleting user from DB, message will automatically deleted in 3 sec")
user_identifier_prompt = hbold("Enter user_id (int) or username (str) user which you would like to")