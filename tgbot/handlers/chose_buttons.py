from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message

from tgbot.keyboards.chose_data_user import data_select_keyboard, create_data_select_keyboard
from tgbot.misc.User_State import UserState
from tgbot.services.db_api import DataBase
from tgbot.texts.functions_texts import user_identifier_prompt


def get_info_user(dp: Dispatcher):
    db = DataBase()

    @dp.callback_query_handler(text="info_user")
    async def set_user_id(call: CallbackQuery):
        await call.message.answer(text="Please chose date which you would like to get",
                                  reply_markup=data_select_keyboard)

    @dp.callback_query_handler(text=["user_id", "username", "full_name", "lang_code", "is_premium", "registered_time"])
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

    @dp.callback_query_handler(text="all_data")
    async def select_all_data(call: CallbackQuery, state: FSMContext):
        data_to_update = {
            'user_id_select': True,
            'username_select': True,
            'full_name_select': True,
            'lang_code_select': True,
            'is_premium_select': True,
            'registered_time_select': True,
            'all_data': True,
        }
        await state.update_data(**data_to_update)

        updated_keyboard = await create_data_select_keyboard(state)
        await call.message.edit_reply_markup(reply_markup=updated_keyboard)

    @dp.callback_query_handler(text="clear_all_data")
    async def clear_all_data(call: CallbackQuery, state: FSMContext):
        data_to_clear = {
            'user_id_select': False,
            'username_select': False,
            'full_name_select': False,
            'lang_code_select': False,
            'is_premium_select': False,
            'registered_time_select': False,
            'all_data': False,
        }
        await state.update_data(**data_to_clear)

        updated_keyboard = await create_data_select_keyboard(state)
        await call.message.edit_reply_markup(reply_markup=updated_keyboard)

    @dp.callback_query_handler(text="finish")
    async def process_finish(call: CallbackQuery):
        await call.message.answer(text=user_identifier_prompt)

        await UserState.user_idd.set()

    @dp.message_handler(state=UserState.user_idd)
    async def get_user(message: Message, state: FSMContext):
        user_id = message.text
        await state.update_data(user_id=user_id)
        await state.set_state(None)

        user_data = await state.get_data()

        fields_to_select = []

        for field_name, selected in user_data.items():
            if field_name.endswith('_select') and selected:
                field = field_name.replace('_select', '')
                fields_to_select.append(field)

        field_name_mapping = {
            'user_id': 'User ID',
            'username': 'Username',
            'full_name': 'Full Name',
            'lang_code': 'Language Code',
            'is_premium': 'Premium Status',
            'registered_time': 'Registration Time',
        }

        selected_user_data = db.select_user(user_id=user_id, fields=fields_to_select)

        selected_user_dat = dict(zip(fields_to_select, selected_user_data))

        response_message = "Here is the information you requested: \n"

        for field in fields_to_select:
            field_name = field_name_mapping.get(field, field)

            value = selected_user_dat.get(field, 'N/A')

            if field_name == "Username" and value != "N/A":
                response_message += f"{field_name}: @{value}\n"
            else:
                response_message += f"{field_name}: {value}\n"

        await message.answer(text=response_message)
