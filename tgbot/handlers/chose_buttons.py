from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message

from tgbot.keyboards.chose_data_user import (data_select_keyboard, create_data_select_keyboard)
from tgbot.misc.User_State import UserState


def get_info_user(dp: Dispatcher):
    @dp.callback_query_handler(text="info_user")
    async def set_user_id(call: CallbackQuery):
        await call.message.answer(text="Please chose date which you would like to get",
                                  reply_markup=data_select_keyboard)

    @dp.callback_query_handler(text=["user_id", "username", "fullname", "lang_code", "is_premium", "registered_time"])
    async def toggle_button(call: CallbackQuery, state: FSMContext):
        # Получаем текущее состояние кнопки
        current_state_data = await state.get_data()
        button_state = current_state_data.get(call.data + '_select', False)

        # Переключаем состояние кнопки
        await state.update_data({call.data + '_select': not button_state})

        # Создаем обновленную клавиатуру
        updated_keyboard = await create_data_select_keyboard(state)

        # Обновляем сообщение с новой клавиатурой
        await call.message.edit_reply_markup(reply_markup=updated_keyboard)

    @dp.message_handler(state=UserState.user_idd)
    async def get_user(message: Message, state: FSMContext):
        user_id = message.text
        await state.update_data(user_id=user_id)
        await state.set_state(None)

        user_data = await state.get_data()
        user_id_selected = user_data.get("user_id_select")

        # if user_id_selected:

        # selected_user = db.select_user(user_id=user_id)
        # await message.answer(f"Username: @{selected_user[0][1]}\n"
        #                      f"All user data: {selected_user[0]}")
